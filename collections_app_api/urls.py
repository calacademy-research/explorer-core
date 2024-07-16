from django.urls import path, include
from django.conf import settings
from . import views
from .views import *
from rest_framework import routers


# collectionobj_router = routers.SimpleRouter()
# collectionobj_router.register(
#     r'collections',
#     CollectionObjsViewSet,
#     basename='collections'
# )


urlpatterns = [
    path('get_image', views.get_image),
    path('list_images', views.list_images),
    path('get_collections_data', views.get_collections_data),
    path('get_publications', views.get_publications, name='get_publications'),
    path('get_datasets', views.get_datasets, name='get_datasets'),
    # path('register/', views.create_user),
    # path('login/', views.user_authentication)

    ##added by jz
    path('hello/', views.hello_CAS, name='hello_CAS'),
    path('cluster/', views.db_check, name='cluster_test'),
    path('coordinates/', views.db_coordinates, name="db_coordinates"),
    path('collection_objects/', views.db_collectionobjects, name="collections_graph_year"),
    path('collection/', views.db_collection, name="collection_time"),
    path('collection_map/', views.db_collectiongeo, name='collections_map'),
    path('collection_images/', views.db_collectionimages, name='collection_images'),

    path('idig/', views.iDigBioFetch, name='iDigBioFetch'),
    path('raw/', views.view_rawData, name='view_rawData'),
    #path('api/', include(collectionobj_router.urls))
]
