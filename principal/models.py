from django.db import models
# Create your models here.

from django.db import models
class Empresa(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    logo = models.ImageField()
    phone = models.CharField(max_length=50)
    history = models.TextField()
    cod_geography =models.CharField(max_length=50)
def __unicode__(self):
    return self.name