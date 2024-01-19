
from django.shortcuts import render
from .models import Images
from django.utils import timezone
from rest_framework import generics, response
from rest_framework.decorators import api_view
from .serializers import ImageSerializer
from datetime import datetime

@api_view(['GET'])
def get_image(request):

    filepath = request.GET.get('filepath', None)

    if filepath is None:
        return response.Response({'error': 'Parameter "filepath" is required'}, status=400)

    app = Images.objects.filter(internal_filename=filepath)

    if not app.exists():
        return response.Response({'error': 'Image not found'}, status=404)

    serializer = ImageSerializer(app, many=True)
    data = serializer.data
    return response.Response(data)


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

    return response.Response(data)
