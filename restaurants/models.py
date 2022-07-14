from django.db import models


class Davlat(models.Model):
    davlat_nomi = models.CharField(max_length=30)

    def __str__(self):
        return self.davlat_nomi
    

class Viloyat(models.Model):
    davlat = models.ForeignKey(Davlat, on_delete=models.RESTRICT, null=True)
    viloyat = models.CharField(max_length=30)
    
    def __str__(self):
        return self.viloyat
    

class Restaurant(models.Model):
    davlat = models.ForeignKey(Davlat, on_delete=models.RESTRICT, null=True)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.RESTRICT, null=True)
    restarant_nomi = models.CharField(max_length=128)
