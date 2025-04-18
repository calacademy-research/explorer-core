from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from .serializers_og import *

from .serializers_og import *
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
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import pandas as pd
import math
import urllib.parse
from pygbif import species as species
from pygbif import occurrences as occ
from pygbif import registry


class CollectionObjsViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionObjectSerializer
    queryset = Collectionobject.objects.all()

def db_check(request):
    custom_info = request.cluster_info
    return HttpResponse(custom_info)


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

