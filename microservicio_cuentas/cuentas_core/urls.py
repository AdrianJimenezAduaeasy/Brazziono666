"""
URL configuration for cuentas_core project.

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
from . import services
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/crear', services.crear_cuenta, name='crear_cuenta'),
    path('cuentas/actualizar/<int:cuenta_id>', services.actualizar_cuenta, name='actualizar_cuenta'),
    path('cuentas/consultar', services.obtener_cuentas, name='listar_cuentas'),
    path('cuentas/eliminar/<int:cuenta_id>', services.eliminar_cuenta, name='eliminar_cuenta'),
    path('cuentas/consultar/<int:cuenta_id>', services.obtener_cuenta, name='consultar_cuenta'),
    path('cuentas/recargar/<int:cuenta_id>', services.recargar_cuenta, name='recargar_cuenta'),
    path('cuentas/reportes/crear', services.crear_reporte_cuenta, name='crear_reporte'),
    path('cuentas/reportes/consultar', services.consultar_reportes, name='consultar_reportes'),
    path('cuentas/reportes/consultar/<int:cuenta_id>', services.obtener_reportes_cuenta, name='consultar_reportes'),
]
