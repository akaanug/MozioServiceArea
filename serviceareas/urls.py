from django.urls import path, include
from rest_framework import routers
from .views import ServiceAreaViewSet

router = routers.DefaultRouter()
router.register('', ServiceAreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
