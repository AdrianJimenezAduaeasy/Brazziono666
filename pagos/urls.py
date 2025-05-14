# urls.py
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .api import PagoViewSet

router = routers.DefaultRouter()
router.register(r'api/pagos', PagoViewSet, basename='pagos')

urlpatterns = router.urls
