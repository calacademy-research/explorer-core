from django.contrib import admin
from .models import Images
from .models_test import Collectionobject, Collectingevent, Locality, Geography

# Register your models here.
admin.site.register(Images)
admin.site.register(Collectionobject)
