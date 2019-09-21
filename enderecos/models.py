from django.db import models

class Endereco(models.Model):
    linha1 = models.CharField(max_length=200)
    linha2 = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    latitude = models.IntegerField(null=True, blank=True)
    longetude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
