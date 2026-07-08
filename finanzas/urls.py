from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssetViewSet, PriceAlertViewSet

router = DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'alerts', PriceAlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]