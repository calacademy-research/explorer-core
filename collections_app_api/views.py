from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN, HTTP_405_METHOD_NOT_ALLOWED


from django.conf import settings
from django.http import JsonResponse
from django.core.cache import cache
from django.shortcuts import render
from django.db import connection
from django.contrib.auth import authenticate, login

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from collections_app_api.models.modelsCollections import CollectionsAppApiCollectionsrecordset as Recordset
from collections_app_api.models import CollectionsAppApiGalapagateway as GG
from collections_app_api.models.modelsCollections import CollectionsAppApiOccurrence as Occurrence
from collections_app_api.models import CollectionsAppApiSpecies as Species
from collections_app_api.models import CollectionsAppApiOrganization as Org
from .serializers import *

import pandas as pd
import urllib.parse
import logging, re, os, math, json
from pygbif import species as gbif_spec
from pygbif import occurrences as gbif_occ
from pygbif import registry as gbif_reg


from drf_spectacular.utils import extend_schema, OpenApiParameter

logger = logging.getLogger(__name__)

def format_occurrenceID(occurrenceID_raw):
    input_str = occurrenceID_raw.replace(" ", "")
    # regex to match ORN1234, HERP12345, HERP 12345, etc.
    match = re.match(r"([A-Za-z]{3,4})(\d{4,5})", occurrenceID_raw)
    if match:
        letters, numbers = match.groups()
        return f"urn:catalog:CAS:{letters}:{numbers}"
    else:
        raise ValueError("occurrenceID string must contain letters followed by numbers (i.e. ORN1234, ORN 12345, etc.)")

#
# /api/occurrencesDB/
# class OccurrenceViewSet(viewsets.ModelViewSet):
#     queryset = Occurrence.objects.all()
#     serializer_class = OccurrenceSerializer

### api/recordset/
#class CASrecordsetList(generics.ListCreateAPIView):
class CASrecordsetList(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer = RecordsetSerializer
    # logger.info(permission_classes)
    # print(permission_classes)
    def get(self, request, *args, **kwargs):
        # data = cache.get('my_key')
        # if not data:
        #     data = Recordset.objects.values()
        #     cache.set('my_key', data, timeout=60 * 15)  # Cache for 15 minutes
        # return render(request, 'template.html', {'data': data})
        try:
            recordset_list = Recordset.objects.values()
            serializer = RecordsetSerializer(recordset_list, many=True)
            #return Response(queryset, status=status.HTTP_200_OK)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CASoccurrencesList(APIView):
    @extend_schema(
        description='Retrieve a list of occurrences with optional filter by collection ID',
        parameters=[
            OpenApiParameter(
                name='occurrence_id',
                type=str,
                location='body',
                description="ID ({Collection code}{Catalog number}) of the species occurrence(s) to retrieve, no space (i.e. ORN001)."
            ),
        ]
    )

    def get_permissions(self):
        if self.request.method == 'GET':
            # return [IsAuthenticated()]  # Allow authenticated users for GET requests
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAdminUser()]  # Only allow admins for POST requests
        return []

    def get(self, request, occurrence_id=None):
        if occurrence_id:
            logger.info("raw: "+occurrence_id)
            logger.info(occurrence_id[0:15])
            if ":" not in occurrence_id or "urn:catalog:CAS:" not in occurrence_id[:15]:
                logger.info("Need to format occurrence_id")
                occurrence_id = format_occurrenceID(occurrence_id)
                logger.info("clean: "+occurrence_id)
                try:
                    # get specific occurrence by occurrence id (i.e. HERP8141)
                    logger.info(occurrence_id)
                    occurrences_list = Occurrence.objects.filter(occurrence_id=occurrence_id)
                    # return Response(occurrences_list, status=status.HTTP_200_OK)
                    serializer = OccurrenceSerializer(occurrences_list, many=True)
                    # return Response(queryset, status=status.HTTP_200_OK)
                    return Response({"message": "Occurrence details retrieved successfully",
                                     "data": serializer.data},
                                    status=status.HTTP_200_OK)
                except Occurrence.DoesNotExist:
                    return Response({"error": "Occurrence not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # list all occurrences
            occurrences_list = Occurrence.objects.all()
            # return Response(occurrences_list, status=status.HTTP_200_OK)
            serializer = OccurrenceSerializer(occurrences_list, many=True)
            # return Response(queryset, status=status.HTTP_200_OK)
            # return Response(serializer.data)
            return Response({"message": "Occurrence retrieved successfully",
                                    "data": serializer.data},
                                    status = status.HTTP_200_OK)
        #
        # # occurrences_list = Occurrence.objects.values()
        # occurrences_list = Occurrences.objects.all()
        # #return Response(occurrences_list, status=status.HTTP_200_OK)
        # serializer = OccurrenceSerializer(occurrences_list, many=True)
        # #return Response(queryset, status=status.HTTP_200_OK)
        # return Response(serializer.data)

    def post(self, request):

        if not request.user.is_staff: # extra check for admin priv
            return Response({"detail": "Forbidden"}, status=HTTP_403_FORBIDDEN)

        serializer = OccurrenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "New object created successfully",
                             "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({"message": "Validation failed",
                         "errors": serializer.errors},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)

### api/recordset/Galapagateway/occurrences/HERP8141
# class CASrecordsetOccurrence(generics.ListCreateAPIView):
# class CASrecordsetOccurrence(APIView):
#     def get(self, request, recordset_id, occurrence_id, *args, **kwargs):


### api/recordset/Galapagateway/occurrence/
### api/recordset/Galapagateway/occurrence?taxon=
#class CASrecordsetGroupList(generics.ListCreateAPIView):
class CASrecordsetGroupList(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        description='Retrieve a list of occurrences by Recordset Code.',
        request=RecordsetSerializer,
        parameters=[
            OpenApiParameter(
                name='recordset_code',
                type=str,
                location='body',
                description="For example, if you would like to see occurrences/species list of Herpetology, you would use HERP."
            ),
        ]
    )

    def get(self, request, recordset_code, *args, **kwargs):
        if recordset_code.isalpha():
            taxon_key = request.GET.get('taxon', '')

            if recordset_code.lower() in ["gg", "galapagateway"]:
                if len(taxon_key) == 0:

                    # recordset_group = GG.objects.values('occurrence_id', 'taxon_id')
                    recordset_group = GG.objects.values()
                    serialized_data = GalapagatewaySerializer(recordset_group, many=True)
                else:
                    # recordset_group = GG.objects.filter(taxon_id=taxon_key).values('occurrence_id', 'taxon_id')
                    recordset_group = GG.objects.filter(taxon_id=taxon_key).values()

                    serialized_data = GalapagatewaySerializer(recordset_group, many=True)
                #print(recordset_group)
                #return Response(recordset_group, status=status.HTTP_200_OK)
                return Response(serialized_data.data, status=status.HTTP_200_OK)
            elif recordset_code.lower() in ["herp","orn"]:
                if len(taxon_key) == 0:

                    # recordset_occurrences = Occurrence.objects.filter(collection_code=recordset_code).values('occurrence_id', 'taxon_id')
                    recordset_occurrences = Occurrence.objects.filter(collection_code=recordset_code).values()
                else:
                    # recordset_occurrences = Occurrence.objects.filter(collection_code=recordset_code,
                    #                                             taxon_id=taxon_key).values('occurrence_id', 'taxon_id')
                    recordset_occurrences = Occurrence.objects.filter(collection_code=recordset_code,
                                                                      taxon_id=taxon_key).values()
                serializer_occ = OccurrenceSerializer(recordset_occurrences, many=True)
                return Response(serializer_occ.data, status=status.HTTP_200_OK)
                #return Response(recordset_occurrences, status=status.HTTP_200_OK)
            else:
                return Response(f"404: No occurrences in the {recordset_code} collection found with search criteria.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("404: Invalid recordset ID filter", status=status.HTTP_400_BAD_REQUEST)


class CASrecordsetSpeciesList(APIView):
    permission_classes = [AllowAny]
    def get(self, request, recordset_code, *args, **kwargs):

        if recordset_code.isalpha():
                if recordset_code.lower() in ["gg","galapagateway"]:
                    species_group = GG.objects

                    serialized_data = [
                        {"occurrence_id": r.occurrence_id,
                         "scientific_name": r.scientific_name,
                         "taxon": r.taxon_id}
                        for r in species_group]
                    # serialized_data = SpeciesSerializer(species_group, many=True)

                    return Response(serialized_data, status=status.HTTP_200_OK)

                elif recordset_code.lower() in ["herp", "orn"]:
                    recordsets = Occurrence.objects.filter(collection_code=recordset_code)#.values()
                    #recordset_occurrences = recordset_group.values('occurrence_id')
                    # serializer_class = OccurrenceSerializer(recordset_group, many=True)
                    # return Response(serializer_class.data, status=status.HTTP_200_OK)
                    # Serialize the data if needed (assuming you have a serializer)

                    # logger.info(recordsets)
                    #
                    # for every in recordsets:
                    #     logger.info(every)

                    serialized_data = [
                        {"recordset_code": r.collection_code,
                         "occurrence_id": r.occurrence_id,
                         "scientific_name": r.scientific_name,
                         "taxon": r.taxon_id}
                        for r in recordsets]
                    # serialized_data = recordsets

                    return Response(serialized_data, status=status.HTTP_200_OK)

                else:
                    return Response(f"404: No occurrences in the {recordset_code} collection to display, for now.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("404: Invalid recordset ID filter", status=status.HTTP_400_BAD_REQUEST)


### api/recordset/GG/species/beckii
class CASrecordsetSpeciesDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, recordset_code, speciesName_filter, *args, **kwargs):

        if recordset_code.isalpha():
            if speciesName_filter.isalpha():
                if recordset_code.lower() in ["gg", "galapagateway"]:
                    species_group = GG.objects.filter(scientific_name__icontains=speciesName_filter)
                    serialized_data = [
                        {"recordset_id": r.recordset_id,
                         "recordset_code": r.recordsetName_id,
                         "occurrence_id": r.occurrence_id,
                         "scientific_name": r.scientific_name,
                         "taxon": r.taxon_id}
                        for r in species_group]

                    return Response(serialized_data, status=status.HTTP_200_OK)

                elif recordset_code.lower() in ["herp","orn"]:
                    recordsets = Occurrence.objects.filter(collection_code=recordset_code, scientific_name__icontains=speciesName_filter)#.values()
                    #recordset_occurrences = recordset_group.values('occurrence_id')
                    # serializer_class = OccurrenceSerializer(recordset_group, many=True)
                    # return Response(serializer_class.data, status=status.HTTP_200_OK)
                    # Serialize the data if needed (assuming you have a serializer)
                    #print(recordsets)
                    serialized_data = [
                        {"recordset_id": r.recordsetName_id,
                         "recordset_code": r.collection_code,
                         "occurrence_id": r.occurrence_id,
                         "scientific_name": r.scientific_name,
                         "taxon": r.taxon_id}
                        for r in recordsets]

                    return Response(serialized_data, status=status.HTTP_200_OK)

                else:
                    return Response(f"404: No occurrences in the {recordset_code} collection to display, for now.", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(f"404: Please only include alphabetical characters for Scientific Name.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("404: Invalid recordset ID filter", status=status.HTTP_400_BAD_REQUEST)



def rawData():
    # headers = ['id', 'modified', 'license', 'institutionID', 'collectionID', 'institutionCode', 'collectionCode',
    # 'basisOfRecord', 'occurrenceID', 'catalogNumber', 'recordNumber', 'recordedBy', 'sex', 'lifeStage',
    # 'preparations', 'associatedSequences', 'occurrenceRemarks', 'year	month', 'day', 'verbatimEventDate', 'habitat',
    # 'higherGeography', 'continent', 'waterBody', 'islandGroup', 'island', 'country', 'stateProvince', 'county',
    # 'locality', 'verbatimLocality', 'minimumElevationInMeters', 'maximumElevationInMeters', 'verbatimElevation',
    # 'decimalLatitude', 'decimalLongitude', 'geodeticDatum', 'coordinateUncertaintyInMeters', 'verbatimCoordinateSystem',
    # 'georeferenceSources', 'georeferenceRemarks', 'typeStatus', 'identifiedBy', 'dateIdentified', 'scientificName',
    # 'higherClassification', 'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'specificEpithet', 'infraspecificEpithet']
    headers = ['id', 'modified', 'license', 'institutionID', 'collectionID', 'institutionCode', 'collectionCode', 'basisOfRecord', 'occurrenceID', 'catalogNumber', 'recordNumber', 'recordedBy', 'sex', 'lifeStage', 'preparations', 'associatedSequences', 'occurrenceRemarks', 'year	month', 'day', 'verbatimEventDate', 'habitat', 'higherGeography', 'continent', 'waterBody', 'islandGroup', 'island', 'country', 'stateProvince', 'county', 'locality', 'verbatimLocality', 'minimumElevationInMeters', 'maximumElevationInMeters', 'verbatimElevation', 'decimalLatitude', 'decimalLongitude', 'geodeticDatum', 'coordinateUncertaintyInMeters', 'verbatimCoordinateSystem','georeferenceSources', 'georeferenceRemarks', 'typeStatus', 'identifiedBy', 'dateIdentified', 'scientificName', 'higherClassification', 'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'specificEpithet', 'infraspecificEpithet']
    # 54 columns
    #print(len(headers))

    # Construct the file path
    txt_path = os.path.join(settings.BASE_DIR, 'collections_app_api', 'data', 'herp_occurrence.txt')

    # Read the TXT file into a DataFrame with tabs as the separator
    df = pd.read_csv(txt_path, delimiter='\t', low_memory=False)

    # Convert the DataFrame to a dictionary
    data_dict = df.to_dict(orient='list')

    return data_dict

def view_rawData(request):
    data_dict = rawData()
    #print(data_dict.keys())

    # dict_keys(['id', 'modified', 'license', 'institutionID', 'collectionID', 'institutionCode', 'collectionCode',
    #            'basisOfRecord', 'occurrenceID', 'catalogNumber', 'recordNumber', 'recordedBy', 'sex', 'lifeStage',
    #            'preparations', 'associatedSequences', 'occurrenceRemarks', 'year', 'month', 'day', 'verbatimEventDate',
    #            'habitat', 'higherGeography', 'continent', 'waterBody', 'islandGroup', 'island', 'country',
    #            'stateProvince', 'county', 'locality', 'verbatimLocality', 'minimumElevationInMeters',
    #            'maximumElevationInMeters', 'verbatimElevation', 'decimalLatitude', 'decimalLongitude', 'geodeticDatum',
    #            'coordinateUncertaintyInMeters', 'verbatimCoordinateSystem', 'georeferenceSources',
    #            'georeferenceRemarks', 'typeStatus', 'identifiedBy', 'dateIdentified', 'scientificName',
    #            'higherClassification', 'kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'specificEpithet',
    #            'infraspecificEpithet'])

    # print(len(data_dict)) = 55

    #print(len(data_dict['id'])) = 320148

    return JsonResponse(data_dict)


def iDigBioFetch(request):
    idigURL = "https://search.idigbio.org/v2/search/records/"

    rq = {'institutioncode': 'Cas',
          'collectionCode': 'Herp'
          }
    #rq_encoded = urllib.parse.urlencode(rq)
    #print(rq_encoded)
    #rq_encoded = "?rq=%7B%22institutioncode%22%3A+%22Cas%22%7D"
    rq_encoded = "?rq=%7B%22institutioncode%22%3A+%22Cas%22,%22collectioncode%22%3A+%22Herp%22,%22stateprovince%22%3A+%22Galapagos+Prov.%22%7D"
    #print(idigURL+rq_encoded)
    reqresponse = requests.get(idigURL + rq_encoded + "&limit=5000")
    response = reqresponse.json().get('items', [])
    #print(type(response))
    #print(len(response))
    # print(response[0].keys())
    # print(response[0]["data"]["dwc:stateProvince"])
    galapa_list = []
    for every_item in response:
        #print(every_item["data"]["dwc:stateProvince"])
        if "dwc:stateProvince" in every_item["data"].keys():
            if "Galapagos" in every_item["data"]["dwc:stateProvince"]:
                galapa_list.append(every_item)
            if 'urn:catalog:CAS:HERP:8120' in every_item['data']['dwc:occurrenceID']:
                # print(every_item)
                # print('====================================')
                # print('\n')

                # print(every_item.keys()) =
                ## dict_keys(['uuid', 'type', 'etag', 'data', 'indexTerms'])

                # print(every_item['data'].keys()) =
                ## dict_keys(['dwc:specificEpithet', 'dwc:kingdom', 'dwc:recordedBy',
                ### 'dwc:georeferenceSources', 'dwc:order', 'dwc:islandGroup',
                ### 'dwc:occurrenceID', 'id', 'dwc:stateProvince', 'dwc:collectionID',
                ### 'dwc:institutionCode', 'dwc:country', 'dwc:collectionCode',
                ### 'dwc:higherClassification', 'dwc:decimalLatitude', 'dwc:occurrenceRemarks',
                ### 'dwc:waterBody', 'dwc:basisOfRecord', 'dwc:genus', 'dwc:preparations',
                ### 'dwc:sex', 'dcterms:license', 'dwc:phylum', 'dwc:locality', 'dwc:institutionID',
                ### 'dwc:island', 'dwc:geodeticDatum', 'dwc:class', 'dwc:catalogNumber', 'dwc:higherGeography',
                ### 'dwc:month', 'dwc:decimalLongitude', 'dwc:verbatimLocality', 'dwc:verbatimEventDate',
                ### 'dwc:family', 'dcterms:modified', 'dwc:scientificName', 'dwc:day', 'dwc:year'])

                #print(every_item['indexTerms'].keys()) =
                # dict_keys(['geopoint', 'family', 'recordset', 'dqs', 'stateprovince', 'phylum', 'waterbody', 'catalognumber',
                #      'startdayofyear', 'specificepithet', 'continent', 'datemodified', 'uuid', 'countrycode',
                #      'basisofrecord', 'collector', 'institutioncode', 'verbatimlocality', 'datecollected', 'etag',
                #      'hasMedia', 'hasImage', 'kingdom', 'highertaxon', 'collectionid', 'scientificname', 'indexData',
                #      'class', 'occurrenceid', 'institutionid', 'country', 'locality', 'collectioncode', 'flags',
                #      'verbatimeventdate', 'recordids', 'genus', 'order'])

                print(every_item['data'])
                print('------------------------------------')
                print(every_item['indexTerms'])

    # print(len(galapa_list))
    # print(galapa_list[0])
    # print(galapa_list[0].keys())
    #
    # print('\n')
    # print(galapa_list[0]['data'])
    # print(galapa_list[0]['data'].keys())
    # print('\n')

    return JsonResponse(json.dumps(galapa_list), safe=False)


datasetKey_GBIF = {
            'HERP': 'cece4fc2-1fec-4bb5-a335-7252548e3f0b',
            'ORN': '4f29b6ab-20c0-4479-8795-4915bedcebd1',
            'BOT': 'f934f8e2-32ca-46a7-b2f8-b032a4740454',
            'SUR': 'cece4fc2-1fec-4bb5-a335-7252548e3f0b',
        }

organizationKey_GBIF = {
    "CAS": "66522820-055c-11d8-b84e-b8a03c50a862",
}


class pygbifLookup(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):

        # search through records published by California Academy of Sciences's only
        GBIF_CAS_datasets = gbif_reg.dataset_suggest(publishingOrg='66522820-055c-11d8-b84e-b8a03c50a862')
        splist = ["Chelonoidis vandenburghi (Desola, 1930)", "Amblyrhynchus cristatus jeffreysi Miralles & Macleod"]
        taxonKeys = [species.name_backbone(x)['usageKey'] for x in splist]
        logger.info(taxonKeys)
        out = [gbif_occ.search(taxonKey=x, limit=0)['count'] for x in taxonKeys]
        logger.info(out)
        x = dict(zip(splist, out))
        sorted(x.items(), key=lambda z: z[1], reverse=True)
        logger.info(len(GBIF_CAS_datasets))
        #return JsonResponse(x, safe=False)
        return Response(GBIF_CAS_datasets)


class GBIFrecordsetSpeciesList(APIView):
    def get(self, request, species_name, *args, **kwargs):
        # print(species_name)
        speciesinfo = gbif_spec.name_backbone(species_name)

        # print(speciesinfo)
        ## usageKey == taxonKey
        # taxonKey = species.name_backbone(species_name)['usageKey']
        # taxonResponse = {
        #     species_name: str(taxonKey)
        #             }

        return Response(speciesinfo)

# class GBIFrecordsetList(APIView):
#     def get(self, request, *args, **kwargs):
#
#         ##ideally in production will include all of CAS occurrences
#         ##currently focused on two CAS HERP specimen
#
#         # gbif8141 = "&occurrenceId=" + "urn%3Acatalog%3ACAS%3AHERP%3A8141"
#         # gbif10615 = "&occurrenceId=" + "urn%3Acatalog%3ACAS%3AHERP%3A10615"
#         # URL = 'http://api.gbif.org/v1/occurrence/search/?dataset_key=cece4fc2-1fec-4bb5-a335-7252548e3f0b&has_geospatial_issue=false&geometry=POLYGON((-92.05308%201.05899,-92.577%20-0.45108,-89.34099%20-3.62304,-88.78625%201.05899,-92.05308%201.05899))&occurrence_status=present&occurrenceId=urn%3Acatalog%3ACAS%3AHERP%3A8141&occurrenceId=urn%3Acatalog%3ACAS%3AHERP%3A10615'
#         # response = requests.get(URL)
#         #
#         # if response.status_code == 200:
#         #     return Response(response.json(), status=status.HTTP_200_OK)
#         # else:
#         #     return Response(response.json(), status=response.status_code)
#
#         #result = occ.search(occurrenceId=['urn:catalog:CAS:HERP:8141','urn:catalog:CAS:HERP:10615'])
#
#         recordsets = Recordset.objects.all()
#         recordsets_data =
#         return Response(recordsets_data)

class GBIFrecordsetGroupList(APIView):
    def get(self, request, datasetID, *args, **kwargs):

        ##have to consider limit=300, integrate offset param and pagination

        URL = 'http://api.gbif.org/v1/occurrence/search/?'
        paramsGroup = {
            'dataset_key': datasetKey_GBIF[datasetID.upper()],
        }
        response = requests.get(URL, params=paramsGroup)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)

class GBIFrecordsetOccurrence(APIView):
    permission_classes = [AllowAny]
    def get(self, request, filter, *args, **kwargs):

        logger.info(f'GBIFrecordsetOccurrence search filter: {filter}')
        # if filter.isdigit():
        #     taxonID = filter
        #     # result = occ.search(datasetKey=datasetID, taxonKey=taxonID)
        #     logger.info(f'[[Searching GBIF records with taxon ID....]]')
        #     result = gbif_occ.search(publishingOrgKey=organizationKey_GBIF['CAS'], taxonKey=taxonID)
        if filter[:1].isalpha():
            logger.info('[[Searching GBIF records with occurrence ID....]]')
            if 'urn:catalog:' in filter:
                occurrenceID = filter
                # logger.info(f'Complete occurrenceID detected as filter')
            else:
                occurrenceID = format_occurrenceID(filter)
                logger.info(f'Formatted occurrenceID: {occurrenceID}')
            # result = occ.search(datasetKey=datasetID, occurrenceID=occurrenceID)
            #result = occ.search(scientificName=speciesName)
            result_gbifocc = gbif_occ.search(publishingOrgKey=organizationKey_GBIF['CAS'], occurrenceID=occurrenceID)
        #result = occ.search()
        #return Response(":-)")
        else:
            result_gbifocc = "No results from GBIF occurrence search. Retry with occurrence ID in full format (i.e. urn:catalog:CAS:HERP:1234) or shorthand (i.e. HERP1234)."
        return Response(result_gbifocc['results'][0])

#
# class LoginView(APIView):
#     permission_classes = [AllowAny]  # Allow all users (authenticated or not) to access this view
#
#     def post(self, request, *args, **kwargs):
#         username = request.data.get("username")
#         password = request.data.get("password")
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)