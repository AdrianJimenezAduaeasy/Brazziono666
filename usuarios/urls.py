from rest_framework import routers
from .api import RegisterViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

router = routers.DefaultRouter()
router.register(r'api/usuarios', RegisterViewSet, basename='usuarios')

urlpatterns = router.urls + [
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]
