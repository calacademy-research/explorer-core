from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


from django.conf import settings
from django.http import JsonResponse
from django.core.cache import cache
from django.shortcuts import render
from django.db import connection
from django.contrib.auth import authenticate, login

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from .models import CollectionsAppApiCollectionsrecordset as Recordset
from .models import CollectionsAppApiGalapagateway as GG
from .models import CollectionsAppApiOccurrence as Occurrence
from .models import CollectionsAppApiSpecies as Species
from .models import CollectionsAppApiOrganization as Org
from .serializers import *

import json
import os
import pandas as pd
import math
import urllib.parse
from pygbif import species as species
from pygbif import occurrences as occ
from pygbif import registry
import logging

logger = logging.getLogger(__name__)

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
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        occurrences_list = Occurrence.objects.values()
        #return Response(occurrences_list, status=status.HTTP_200_OK)
        serializer = OccurrenceSerializer(occurrences_list, many=True)
        #return Response(queryset, status=status.HTTP_200_OK)
        return Response(serializer.data)

### api/recordset/Galapagateway/occurrences/HERP8141
# class CASrecordsetOccurrence(generics.ListCreateAPIView):
# class CASrecordsetOccurrence(APIView):
#     def get(self, request, recordset_id, occurrence_id, *args, **kwargs):


### api/recordset/Galapagateway/occurrence/
### api/recordset/Galapagateway/occurrence?taxon=
#class CASrecordsetGroupList(generics.ListCreateAPIView):
class CASrecordsetGroupList(APIView):
    permission_classes = [AllowAny]
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


datasetKey_match = {
            'HERP': 'cece4fc2-1fec-4bb5-a335-7252548e3f0b',
            'ORN': '4f29b6ab-20c0-4479-8795-4915bedcebd1',
            'BOT': 'f934f8e2-32ca-46a7-b2f8-b032a4740454',
        }

organizationKey_GBIF = {
    "CAS": "66522820-055c-11d8-b84e-b8a03c50a862",
}

GBIF_CAS_datasets = []

class pygbifTester(APIView):
    def get(selfself, request, *args, **kwargs):

        GBIF_CAS_datasets = registry.dataset_suggest(publishingOrg='66522820-055c-11d8-b84e-b8a03c50a862')
        splist = ["Chelonoidis vandenburghi (Desola, 1930)", "Amblyrhynchus cristatus jeffreysi Miralles & Macleod"]
        taxonKeys = [species.name_backbone(x)['usageKey'] for x in splist]
        print(taxonKeys)
        out = [occ.search(taxonKey=x, limit=0)['count'] for x in taxonKeys]
        print(out)
        x = dict(zip(splist, out))
        sorted(x.items(), key=lambda z: z[1], reverse=True)
        print(len(GBIF_CAS_datasets))
        #return JsonResponse(x, safe=False)
        return Response(GBIF_CAS_datasets)

class GBIFrecordsetSpeciesList(APIView):
    def get(self, request, species_name, *args, **kwargs):
        # print(species_name)
        speciesinfo = species.name_backbone(species_name)

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
            'dataset_key': datasetKey_match[datasetID.upper()],
        }
        response = requests.get(URL, params=paramsGroup)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)

class GBIFrecordsetOccurrence(APIView):
    def get(self, request, datasetID, filter, *args, **kwargs):

        print("GBIFrecordsetOccurrence search filter: ", filter)

        if filter.isdigit():
            taxonID = filter
            result = occ.search(datasetKey=datasetID, taxonKey=taxonID)
        elif filter[:4].isalpha():
            speciesName = filter
            result = occ.search(datasetKey=datasetID, scientificName=speciesName)
            #result = occ.search(scientificName=speciesName)
        #result = occ.search()
        #return Response(":-)")
        else:
            result = "No results from occurrence search. Retry with either taxonKey or species' scientific name."
        return Response(result)

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