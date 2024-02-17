from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('get_image', views.get_image),
    path('list_images', views.list_images),
    path('get_collections_data', views.get_collections_data),
    path('get_pubs', views.get_publications),
    path('get_datasets', views.get_datasets)
    # path('register/', views.create_user),
    # path('login/', views.user_authentication)

]
