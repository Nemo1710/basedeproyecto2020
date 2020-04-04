from django.contrib import admin

# Register your models here.
from .models import CasosPorProvincia,DatosCOVID

admin.site.register(CasosPorProvincia)
admin.site.register(DatosCOVID)