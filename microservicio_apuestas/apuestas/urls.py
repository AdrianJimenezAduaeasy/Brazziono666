from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='apuestas_home'),
    path('realizar/', views.realizar_apuesta, name='realizar_apuesta'),
    path('listar/', views.listar_apuestas, name='listar_apuestas'),
    path('<int:id>/', views.detalle_apuesta, name='detalle_apuesta'),
    path('actualizar/<int:id>/', views.actualizar_estado, name='actualizar_estado'),
]
