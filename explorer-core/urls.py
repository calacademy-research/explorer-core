"""
URL configuration for explorer-core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.http import HttpResponse

urlpatterns = [path('', lambda request: HttpResponse("Collection Explorer Homepage"), name='home'),
               path('api/', include("collections_app_api.urls")),
               path("admin/", admin.site.urls),
               path('accounts/', include("django.contrib.auth.urls")),
               # path('api-auth/', include('rest_framework.urls')),  # DRF's login/logout views
               path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
               path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
              ]
