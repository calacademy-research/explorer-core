from django.urls import path, include
from django.conf import settings
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import CASrecordsetList, CASoccurrencesList, CASrecordsetGroupList, CASrecordsetSpeciesList, \
    CASrecordsetSpeciesDetail, GBIFrecordsetOccurrence
#from .views import OccurrenceViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# collectionobj_router = routers.SimpleRouter()
# collectionobj_router.register(
#     r'collections',
#     CollectionObjsViewSet,
#     basename='collections'
# )

# router = DefaultRouter()
# router = SimpleRouter()
# router.register(r'GalapaGateway', )
#router.register(r'recordsetAPI', CASrecordsetList)
# router.register(r'occurrencesDB', OccurrenceViewSet, basename='occurrences')
# router.register(r'groupAPI', CASrecordsetGroupList)
# router.register(r'speciesAPI', CASrecordsetSpeciesList)

urlpatterns = [
    # path('', include(router.urls)),
    #path('login/', LoginView.as_view(), name='api-login'),
    #path ('logout/'. )
    # path('idig/', views.iDigBioFetch, name='iDigBioFetch'),
    # path('raw/', views.view_rawData, name='view_rawData'),
    #path('pygbif/', pygbifTester.as_view(), name='pygbif'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('recordset/', CASrecordsetList.as_view(), name='recordset-list'),
    path('recordset/<str:recordset_code>/occurrences/', CASrecordsetGroupList.as_view(), name='recordset-occurrences'),
    path('recordset/<str:recordset_code>/species/', CASrecordsetSpeciesList.as_view(), name="recordset-species"),
    path('recordset/<str:recordset_code>/species/<str:speciesName_filter>', CASrecordsetSpeciesDetail.as_view(), name="species-detail"),
    path('occurrences/', CASoccurrencesList.as_view(), name='occurrences-list'),
    path('occurrences/<str:occurrence_id>/details', CASoccurrencesList.as_view(), name='occurrences-detail'),
    ##path('api/recordset/<str:recordsetID>/occurrence/<str:filter>/', CASrecordsetOccurrence.as_view(), name='recordset-occurrence'),
    ##path('api/recordset/<str:recordsetID>/occurrence/<str:filter>/media/', CASrecordsetOccurrenceMedia.as_view(), name='recordset-occurrence-media'),

    # path('gbif/', pygbifLookup.as_view(), name='gbif-lookup'),
    path('gbif/<str:filter>/', GBIFrecordsetOccurrence.as_view(), name='gbif-occurrence-lookup'),


    #path('api/', include(collectionobj_router.urls))
]