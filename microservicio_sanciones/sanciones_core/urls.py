"""
URL configuration for sanciones_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .services import aplicar_sancion_servicio, listar_sanciones_servicio, actualizar_sancion_servicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sanciones/', aplicar_sancion_servicio, name='aplicar-sancion-servicio'),
    path('sanciones/listar/', listar_sanciones_servicio, name='listar_sanciones'),
    path('sanciones/actualizar/<int:sancion_id>/', actualizar_sancion_servicio, name='actualizar_sancion'),
]
