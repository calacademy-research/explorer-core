from rest_framework import serializers
from .models_test import *

class GeographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography
        #fields = '__all__'
        fields = ['abbrev', 'centroidlat', 'centroidlon', 'commonname']


class CollectionObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectionobject
        #fields = '__all__'
        fields = ['timestampcreated']

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['username', 'email', 'password', 'is_staff', 'is_active']
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = UserProfile.objects.create_user(**validated_data)
#         return user
#
#
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

