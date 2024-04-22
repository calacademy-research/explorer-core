
from .models import Images

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import *

from .serializers_test import *
from rest_framework import viewsets

from django.conf import settings
from django.utils import timezone
from .middleware import *
from django.db import connections
from django.db.models import Count
from rest_framework import permissions

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import datetime
import timeit
from django_plotly_dash import DjangoDash
import plotly.graph_objs as bar
import plotly.express as bar_long
from collections import defaultdict
import calendar

import requests
import json


class CollectionObjsViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionObjectSerializer
    queryset = Collectionobject.objects.all()

##added by jz
@api_view(['GET'])
def hello_CAS(request):
    return HttpResponse("Hello, CAS!")

@api_view(['GET'])
def db_coordinates(request):
    values = Geography.objects.filter(commonname='New Zealand')
    ##data = Geography.objects.commonname.raw("SELECT FullName FROM botanydb.geography WHERE CommonName = 'New Zealand'")[0]
    ##cnx = mysql.connector.connect(database='geography')
    ##cursor_geo = cnx.cursor()
    #cursor = connection.cursor()
    ##cursor_geo.execute('SELECT FullName FROM botanydb.geography')
    ##values = cursor_geo.fetchall()
    serializer = GeographySerializer(values, many=True)
    data = serializer.data
    return JsonResponse(json.dumps(data), safe=False)
    #return HttpResponse(data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def db_collectionimages(request):
    print(request)
    start = timeit.timeit()
    image_file = ""
    file_createddate = ""
    agentname_created = ""
    agentname_image = ""
    collection_desc = ""
    collectingevent_start = ""


    collection_dict = {}
    collection_attachments = Collectionobjectattachment.objects.values('createdbyagentid', 'collectionobjectid', 'attachmentid')[932:982]

    for collection in collection_attachments:
        attachmentid = collection['attachmentid']
        collectionobjectid = collection['collectionobjectid']

        createdagentid = collection['createdbyagentid']


        agent_by_collection = Agent.objects.filter(agentid=createdagentid).values('agentid', 'firstname', 'lastname', 'initials')
        for agent_info in agent_by_collection:
            #agentname_created = agent_info['initials']
            agentname_created = agent_info['firstname'][0] + ". "  + agent_info['lastname']

        object_by_collection_att = Collectionobject.objects.filter(collectionobjectid=collectionobjectid).values('collectionobjectid', 'catalogeddate', 'text1', 'collectingeventid')

        for object in object_by_collection_att:
            #print('collectionobjectid: ', object['collectionobjectid'])
            collection_desc = object['text1']
            catalogeddate = object['catalogeddate']
            collectingeventid = object['collectingeventid']

            event_by_collecting_att = Collectingevent.objects.filter(collectingeventid=collectingeventid).values('collectingeventid', 'startdate')
            for event in event_by_collecting_att:
                collectingevent_start = event['startdate']

        attachment_by_collection = Attachment.objects.filter(attachmentid=attachmentid).values('attachmentid', 'filecreateddate',
                                                                         'remarks', 'createdbyagentid')
        for attachment in attachment_by_collection:
            #print('attachmentid: ', attachment['attachmentid'])
            image_file = attachment['remarks']
            file_createddate = attachment['filecreateddate']
            agentid_att = attachment['createdbyagentid']
            #print('attachment agentid: ', agentid_att)

            agent_by_attachment = Agent.objects.filter(agentid=agentid_att).values('agentid', 'firstname', 'lastname', 'initials')
            for agent in agent_by_attachment:
                #agentname_image = agent['initials']
                agentname_image = agent['firstname'][0] + " " + agent['lastname']

        if catalogeddate!=None:
            catalogeddate_str = catalogeddate.strftime('%m/%d/%Y')
        if file_createddate!=None:
            file_createddate_str = file_createddate.strftime('%m/%d/%Y')
        if collectingevent_start!=None:
            collectingevent_start_str = collectingevent_start.strftime('%m/%d/%Y')

        collection_dict[collectionobjectid] = {
            'attachmentid': attachmentid,
            'file_createddate': file_createddate_str,
            'image_file': image_file,
            'catalogeddate': catalogeddate_str,
            'collection_desc': collection_desc,
            'collectingevent_start': collectingevent_start_str,
            'agentname_collection': agentname_created,
            'agentname_image': agentname_image,
    }

    end = timeit.timeit()
    print("Finished in " + str(end - start) + " seconds.")
    json_data = json.dumps(collection_dict)
    return JsonResponse(json_data, safe=False)

@api_view(['GET'])
def db_collectiongeo(request):
    start = timeit.timeit()
    localityid_str = ""
    lat = ""
    long = ""
    geographid_str = ""
    geographyid_str = ""
    geoname = ""
    geography_name = ""
    eventid = ""
    collectingstart = ""
    collection_list = []
    collectingEvent = Collectingevent.objects.all()[:1000]
    for event in collectingEvent:
        #print(event.collectingeventid)
        eventid = event.collectingeventid
        #print(event.startdate)
        collectingstart = event.startdate
        locality_item = event.localityid
        # locality_str = str(localityid)
        # print(locality_str)
        #print(localityid.values('localityid'))
        #print(locality_item.localityid)
        localityid = locality_item.localityid
        #print('here ' + str(localityid))
        #locality_item = event.objects.get(pk=localityid)
        locality_by_event = Locality.objects.filter(localityid=localityid).values('localityid', 'latitude1','longitude1', 'geographyid')
        #locality_by_event = Locality.objects.filter(localityid=localityid).all()
        for local in locality_by_event:
            #print(local.latitude1)
            #print(local)
            geographyid = local['geographyid']
            lat = local['latitude1']
            long = local['longitude1']
            # print("Latitude: " + str(lat))
            # print("Longitude: " + str(long))
            # print(geographyid)
            geography_by_locality = Geography.objects.filter(geographyid=geographyid).values('geographyid', 'fullname')
            for geo in geography_by_locality:
                #print(geo)
                geoid = geo['geographyid']
                geoname = geo['fullname']
        #print(collectingstart)
        if collectingstart!=None:
            collection_list.append([eventid, collectingstart.strftime('%m/%d/%Y'), localityid, geographyid, lat, long, geoname])
        else:
            print(eventid)
            print(collectingstart)
            print(localityid)
            print(geoname)
            collection_list.append([eventid, 'Unknown', localityid, geographyid, int(0), int(0), geoname])
                # print(geoid)
                # print(geoname)
    # geography = Geography.objects.all()
    # for geo in geography:
    #     print(geo.fullname)
    #     print(geo.geographyid)
    #     geoID = geo.objects.get(pk=localityid)
    #     localityid = geoID.localityid.all()
    #     for loc in localityid:
    #         print(loc.geographyid)
    #         print(loc.localityid)
    #         lat = loc.latitude1
    #         long = loc.longitude1
    #         print("Latitude: " + str(loc.latitude1))
    #         print("Longitude: " + str(loc.longitude1))
    #         collectingevent_set = loc.collecting.all()
    #         for geoID in geographyid_set:
    #             print(geoID.geographyid)
    #             print(geoID.fullname)
    end = timeit.timeit()
    print(collection_list)
    print("Finished in " + str(start-end) + " seconds.")
    return HttpResponse("yippie!")


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def db_collection(request):
    collection_data = Collectionobject.objects.values('collectionobjectid', 'catalogeddate', 'countamt')
    line_dict = {}

    for each in collection_data:
         if (each['catalogeddate'] != None) and (each['countamt'] != None):
             date_item = each['catalogeddate']
             # print(date_item)
             # print(each['countamt'])
             line_dict[date_item] = line_dict.get(date_item, 0) + each['countamt']

    #json_data = json.dumps(line_dict)
    #print(json_data)

    #sorted(line_dict, key=line_dict.get)
    sorted_collections = dict(sorted(line_dict.items(), key=lambda item: item[0]))

    x_values = list(sorted_collections.keys())
    y_values = list(sorted_collections.values())

    collections_over_time = {
        'Date': x_values,
        'Collections': y_values,
    }

    return JsonResponse(collections_over_time, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def db_collectionobjects(request):
    #values = Collectionobject.objects.all().values_list('timestampcreated')[:1000]

    collections_by_year_month = defaultdict(lambda: defaultdict(int))
    start = timeit.timeit()
    year = request.GET.get('year')
    if year:
        date_counts = Collectionobject.objects.filter(catalogeddate__year=year).values('collectionobjectid', 'catalognumber','catalogeddate').annotate(date_count=Count('catalogeddate'))
        date_consolidated = {}

        for collection in date_counts:
            for each, thing in collection.items():
                if each == "catalogeddate":
                    date_item = thing
                    month_x = date_item.strftime('%b')
                if each == 'date_count':
                    amount_item = thing
            date_consolidated[month_x] = date_consolidated.get(month_x, 0) + amount_item

        x_data = list(date_consolidated.keys())
        x_data.sort()
        y_data = list(date_consolidated.values())

        collections_by_year_month = {
             'Month': x_data,
             'Collections': y_data,
         }

    else:
        date_counts = Collectionobject.objects.values('collectionobjectid', 'catalognumber', 'catalogeddate', 'catalogeddate__year', 'catalogeddate__month').annotate(date_count=Count('catalogeddate'))#.order_by('-catalogeddate__year')
        date_consolidated = {}

        for item in date_counts:
            if item['catalogeddate']!=None:
                year_item = item['catalogeddate__year']
                month_item = datetime.date(2024, item['catalogeddate__month'],1).strftime('%B')
                collections_by_year_month[month_item][year_item] += item['date_count']

        months = list(collections_by_year_month.keys())
        years = list(set(year for year_col in collections_by_year_month.values() for year in year_col.keys()))
        month_names = calendar.month_name[1:]
        sorted_months = sorted(months, key=lambda x: month_names.index(x), reverse=True)

        bar_traces = []
        collections_data = [[collections_by_year_month[month].get(year,0) for year in years] for month in sorted_months]

    json_data = json.dumps(collections_by_year_month)
    return JsonResponse(json_data, safe=False)

##


# @api_view(['POST'])
# def create_user(request):
#     if request.method == 'POST':
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'sucess': 'user created'}, status=200)
#         return Response({'error': 'user creation failed'}, status=404)
#
#
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def user_authentication(request):
#     if request.method == 'POST':
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#
#             # Authenticate user
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 # Generate or get an existing token
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key})
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=401)
#         return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_image(request):

    filepath = request.GET.get('filepath', None)

    if filepath is None:
        return Response({'error': 'Parameter "filepath" is required'}, status=400)

    app = Images.objects.filter(internal_filename=filepath)

    if not app.exists():
        return Response({'error': 'Image not found'}, status=404)

    serializer = ImageSerializer(app, many=True)
    data = serializer.data
    return Response(data)


@api_view(['GET'])
def list_images(request):

    collection = request.GET.get('collection', None)
    redacted = request.GET.get('redacted', None)
    limit = request.GET.get('limit', 10)
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end', None)


    filter_conditions = {}

    if collection:
       filter_conditions['collection'] = collection

    if redacted:
        filter_conditions['redacted'] = redacted


    if date_start:

        filter_conditions['datetime__gte'] = date_start

    if date_end:

        filter_conditions['datetime__lte'] = date_end



    limit = int(limit)

    app = Images.objects.filter(**filter_conditions)[:limit]

    serializer = ImageSerializer(app, many=True)

    data = serializer.data

    return Response(data)

@api_view(['GET'])
def get_collections_data(request):
    table = request.GET.get("table", None)
    collection = request.GET.get("collection", None)
    columns = request.GET.getlist("columns", None)
    condition = request.GET.get("condition", None)
    limit = request.GET.get("limit", None)

    if not table:
        return Response({'error': 'Parameter "table" is required'}, status=400)

    if not collection:
        return Response({'error': 'Parameter "collection" is required'}, status=400)

    # parsing SQL query
    sql = get_record_sql_parser(table=table, columns=columns,
                                condition=condition, limit=limit)

    try:
        # configuring database connection
        connection = connections[collection]

        with connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        return Response(results)

    except ConnectionError as e:
        return Response({'error': f'Database error: {str(e)}'}, status=500)


@api_view(['GET'])
def get_datasets(request):

    pub_key = request.GET.get("pub_key", None)

    if not pub_key:
        return Response({'error': 'Parameter "pub_key" is required'}, status=400)

    gbif_endpoint = f'https://api.gbif.org/v1/dataset/search'

    params = {'publishing_org': pub_key}
    response = requests.get(gbif_endpoint, params=params)

    if response.status_code == 200:
        datasets = response.json().get('results', [])


        # publications = extract_publications(datasets)
        return Response({'publications': datasets})
    else:
        return Response({'error': 'Failed to fetch data from GBIF'}, status=response.status_code)

#Grab all publications for a given
@api_view(['GET'])
def get_publications(request):
    pub_key = request.GET.get("pub_key", None)
    dataset_key = request.GET.get("dataset_key", None)

    if not pub_key:
        return Response({'error': 'Parameter "pub_key" is required'}, status=400)
    if not dataset_key:
        return Response({'error': 'Parameter "dataset_key" is required'}, status=400)


    gbif_api_url = 'https://api.gbif.org/v1/literature/search'
    params = {'publishingOrganizationKey': pub_key,
              'gbifDatasetKey' : dataset_key,
              'limit': 20}  # Adjust limit as needed

    try:
        response = requests.get(gbif_api_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors from GBIF
        return Response({'error': f'HTTP error from GBIF: {http_err}'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except requests.exceptions.RequestException as e:
        # Handle other request issues, such as network errors
        return Response({'error': f'Request error: {e}'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    datasets = response.json().get('results', [])
    publications = extract_literature(datasets)

    return Response({'publications': publications})





def extract_literature(json_response):

    extracted_details = []

    for publication in json_response:

        title = publication.get('title', 'No title available')
        authors = [f"{author['firstName']} {author['lastName']}" for author in publication.get('authors', [])]
        discovered = publication.get('discovered', 'No discovery date available')
        added = publication.get('added', 'No added date available')
        published = publication.get('published', 'No published date available')

        publication_details = {
            'title': title,
            'authors': authors,
            'discovered': discovered,
            'added': added,
            'published': published
        }

        extracted_details.append(publication_details)

    return extracted_details



# Add image collections as an endpoint

