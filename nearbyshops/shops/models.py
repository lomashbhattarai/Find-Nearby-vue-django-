from django.contrib.gis.db import models

# Create your models here.

class Shop(models.Model):
    name= models.CharField(max_length=100)
    location= models.PointField()
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=50)

class Hospital(models.Model):
    name= models.CharField(max_length=100)
    location= models.PointField()
    address= models.CharField(max_length=100)

class RoadSegment(models.Model):
    ntlclass = models.CharField(max_length=254)
    srftpe = models.CharField(max_length=254)
    segment = models.CharField(max_length=50)
    geom = models.MultiLineStringField()

    def __str__(self):
        return self.segment


class WorldBorder(models.Model):
    name= models.CharField(max_length=50)
    area= models.IntegerField()
    pop2005= models.IntegerField('Popullation 2005')
    fips= models.CharField('FIPS Code',max_length=2)
    iso2= models.CharField('2 Digit ISO',max_length=2)
    iso3= models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name


