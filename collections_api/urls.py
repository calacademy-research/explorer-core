from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('get_image', views.get_image),
    path('list_images', views.list_images),
    path('get_collections_data', views.get_collections_data),
    path('get_publications', views.get_publications, name='get_publications'),
    path('get_datasets', views.get_datasets, name='get_datasets'),
    # path('register/', views.create_user),
    # path('login/', views.user_authentication)
    path('get_expeditions', views.get_expeditions, name='get_expeditions'),
    path('expeditions-per-discipline', views.expeditions_per_discipline, name='expeditions-per-discipline'),

    ##added by jz
    path('/', views.hello_CAS, name='hello_CAS'),
    path('coordinates/', views.db_coordinates, name="db_coordinates")

]