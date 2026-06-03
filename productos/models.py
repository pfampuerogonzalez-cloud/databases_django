from django.db import models

# Create your models here.

#ESTA CLASE LA TOMARA DE EL ORM YL A TRANSFORMARÁ EN TABLE DENTRO DE LA DB
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    



    
