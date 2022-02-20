from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_gis.fields import GeoJsonDict

from providers.models import Provider
from serviceareas.models import ServiceArea
from django.contrib.auth.models import User


class APITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='test',
            email='test@bar.com',
            password='test')
        self.client.force_login(user=self.user)

    def test_create_provider(self):
        data = {'name': 'providertest', 'email': 'pt@e.com', 'language': 'en', 'currency': 'USD'}
        response = self.client.post('/providers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, 'providertest')
        return Provider.objects.get(name='providertest')

    def test_create_servicearea(self):
        provider = self.test_create_provider()
        data = {'name': 'serviceareatest', 'polygon': GeoJsonDict([
            ('type', 'Polygon'),
            ('coordinates', (
                ((11.113727, -32.665789), (11.113727, 96.793794), (69.139097, 95.359043),
                 (71.504009, -86.165808), (11.113727, -32.665789)),
                ((44.668256, 18.536529), (42.545927, 63.056741), (26.579844, 59.187025),
                 (26.422533, 16.092462), (44.668256, 18.536529))))]), 'provider_id': provider.id}
        response = self.client.post('/serviceareas/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().name, 'serviceareatest')

        return ServiceArea.objects.get(name='serviceareatest')

    def test_intersection(self):
        self.test_create_servicearea()
        response = self.client.get('/serviceareas/intercepting_polygons/?point={"lat":12.439558,"lng":-30.033872}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['features']), 1)
