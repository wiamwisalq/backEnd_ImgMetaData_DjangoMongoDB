from django.db import models

# Create your models here.

class Gps_loca(models.Model):
    latitude=models.FloatField()
    longitude=models.FloatField()

class Point(models.Model):
    x=models.FloatField()
    y=models.FloatField()
    def __str__(self):
        return self.x
    
class Polygon(models.Model):
    ref=models.CharField(max_length=100)
    points=models.ManyToManyField(Point)
    def __str__(self):
        return self.ref

class Bbox(models.Model):
    xmin=models.FloatField()
    ymin=models.FloatField()
    xmax=models.FloatField()
    ymax=models.FloatField()

class Object(models.Model):
    str=models.CharField(max_length=100)
    polygon=models.OneToOneField(Polygon,on_delete=models.CASCADE,null=True)
    bbox=models.OneToOneField(Bbox,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.str

class File(models.Model):
    file_url=models.CharField(max_length=500)
    width=models.FloatField()
    height=models.FloatField()
    date_captured=models.DateField()
    Gps_location=models.OneToOneField(Gps_loca,on_delete=models.CASCADE,null=True)
    objets=models.ManyToManyField(Object)
    def __str__(self):
        return self.ref_f


