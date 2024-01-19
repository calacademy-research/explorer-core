from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('get_image', views.get_image),
    path('list_images', views.list_images)
]
