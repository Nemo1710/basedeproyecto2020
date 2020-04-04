from django.db import models

# Create your models here.

class CasosPorProvincia(models.Model):
    Provincia = models.CharField(max_length=100)
    Casos_positivos = models.PositiveIntegerField(blank=True, default=0)
    Actualizado = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.Actualizado)

class DatosCOVID(models.Model):
    Cerco = models.PositiveIntegerField(blank=True, default=0)
    Casos_confirmados = models.PositiveIntegerField(blank=True, default=0)
    En_domicilio = models.PositiveIntegerField(blank=True, default=0)
    Hospitalizados_leves = models.PositiveIntegerField(blank=True, default=0)
    Hospitalizados_críticos = models.PositiveIntegerField(blank=True, default=0)
    Fallecidos = models.PositiveIntegerField(blank=True, default=0)
    Recuperados = models.PositiveIntegerField(blank=True, default=0)
    Actualizado = models.DateTimeField(auto_now_add=False, auto_now=True,blank=True, null=True)

    def __str__(self):
        return str(self.Actualizado)