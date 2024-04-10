from rest_framework import serializers
from .models_test import Geography


class GeographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography
        #fields = '__all__'
        fields = ['abbrev', 'centroidlat', 'centroidlon', 'commonname']

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

