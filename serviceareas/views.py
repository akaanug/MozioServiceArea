import json

from drf_yasg.utils import swagger_auto_schema
from rest_framework import exceptions, permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_gis.pagination import GeoJsonPagination

from .models import ServiceArea
from .serializers import ServiceAreaSerializer

from drf_yasg import openapi

point_param = openapi.Parameter('point', openapi.IN_QUERY, type=openapi.TYPE_STRING,
                                description="Point with latitude (lat) and longitude (lng). "
                                            "Example: {\"lat\":8.123213123,\"lng\":3.8979889}")


class ServiceAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()
    pagination_class = GeoJsonPagination
    permission_classes = [permissions.IsAuthenticated]

    #  Returns the service areas that intercept with the given Point
    @swagger_auto_schema(methods=['get'], manual_parameters=[point_param])
    @action(detail=False, methods=['GET'], name='Get Intercepting Polygons')
    def intercepting_polygons(self, request):
        """
            point -- Point parameter in JSON containing latitude and longitude.
        """
        service_areas = ServiceArea.objects.all()
        point = self.request.query_params.get('point', None)
        if point is None:
            raise exceptions.ValidationError('Point cannot be None')

        try:
            point = json.loads(point)

            if point['lat'] is None or point['lng'] is None:
                raise exceptions.ValidationError('lat or lng cannot be None')
            coordinates = map(float, [point['lat'], point['lng']])
            point_str = 'POINT({})'.format(' '.join(map(str, coordinates)))
        except (ValueError, KeyError, TypeError) as e:
            raise exceptions.ValidationError(
                'invalid point: %s' % e)

        # Find the polygons:
        service_areas = service_areas.filter(polygon__contains=point_str)
        serializer = self.get_serializer(service_areas, many=True)
        return Response(serializer.data)
