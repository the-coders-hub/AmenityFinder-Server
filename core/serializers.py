from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(source='profile.picture')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'picture']