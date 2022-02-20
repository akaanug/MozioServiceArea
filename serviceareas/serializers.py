from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from providers.models import Provider
from providers.serializers import ProviderSerializer
from .models import ServiceArea


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = ProviderSerializer(read_only=True)
    provider_id = PrimaryKeyRelatedField(
        queryset=Provider.objects.all(),
        write_only=True, required=True, source='provider')

    class Meta:
        model = ServiceArea
        fields = '__all__'
        geo_field = 'polygon'
