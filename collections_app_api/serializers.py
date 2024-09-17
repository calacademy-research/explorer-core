from rest_framework import serializers

from .models import CollectionsAppApiCollectionsrecordset as Recordset
from .models import CollectionsAppApiGalapagateway as GG
from .models import CollectionsAppApiOccurrence as Occurrence
from .models import CollectionsAppApiSpecies as Species
from .models import CollectionsAppApiOrganization as Org

class RecordsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordset
        fields = '__all__'

class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = '__all__'


class GalapagatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = GG
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

class OrganizaztionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Org
        fields = '__all__'


