from rest_framework import serializers
from .models import Images

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

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

