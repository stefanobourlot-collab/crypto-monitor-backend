from rest_framework import viewsets
from .models import Asset, PriceAlert
from .serializers import AssetSerializer, PriceAlertSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class PriceAlertViewSet(viewsets.ModelViewSet):
    queryset = PriceAlert.objects.all()
    serializer_class = PriceAlertSerializer