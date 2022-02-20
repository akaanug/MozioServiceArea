from rest_framework import serializers
from .models import Provider


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name', 'email', 'phone_number', 'language', 'currency']
