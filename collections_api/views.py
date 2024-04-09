
from .models import Images
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import *
from django.conf import settings
from django.utils import timezone
from .middleware import *
from django.db import connections
from rest_framework import permissions

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
