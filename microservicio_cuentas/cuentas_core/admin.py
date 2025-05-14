# kyc_core/admin.py
from django.contrib import admin
from .models import Cuenta, ReporteCuenta

admin.site.register(Cuenta)
admin.site.register(ReporteCuenta)
