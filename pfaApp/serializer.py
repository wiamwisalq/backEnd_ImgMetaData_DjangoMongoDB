from dataclasses import fields
from rest_framework import serializers
from pfaApp.models import Gps_loca,File,Point,Polygon,Object,Bbox

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=File
        fields=["id","file_url","width","height","date_captured","Gps_location","objets"]
        depth=2
class Gps_locaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gps_loca
        fields=["id","latitude","longitude"]

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model=Point
        fields=["id","x","y"]
        
class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Polygon
        fields=["id","ref","points"]
        depth=1

class BboxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bbox
        fields=["xmin","ymin","xmax","ymax"]
       
class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Object
        fields=["str","polygon","bbox"]
        depth=1

