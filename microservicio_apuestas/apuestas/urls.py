from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='apuestas_home'),
    path('realizar/', views.realizar_apuesta, name='realizar_apuesta'),
    path('listar/', views.listar_apuestas, name='listar_apuestas'),
]
