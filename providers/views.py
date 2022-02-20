from .serializers import ProviderSerializer
from .models import Provider
from rest_framework import viewsets, permissions


# Create your views here.
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]
