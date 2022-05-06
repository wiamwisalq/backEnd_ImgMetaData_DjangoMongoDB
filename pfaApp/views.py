from rest_framework import viewsets
from rest_framework.response import Response
from pfaApp.models import Gps_loca,File, Object,Point,Polygon,Bbox
from django.shortcuts import render
from .serializer import BboxSerializer, Gps_locaSerializer,FileSerializer, ObjectSerializer, PointSerializer, PolygonSerializer

# Create your views here.

class FileViewSet(viewsets.ModelViewSet):
    
    serializer_class=FileSerializer

    def get_queryset(self):
        files=File.objects.all()
        return files
    def create(self, request, *args, **kwargs):    
        file_data=request.data
        new_gps=Gps_loca.objects.create(latitude=file_data["Gps_location"]["latitude"],longitude=file_data["Gps_location"]["longitude"])
        new_gps.save()
        new_file=File.objects.create(file_url=file_data["file_url"],width=file_data["width"],height=file_data["height"],date_captured=file_data["date_captured"],Gps_location=new_gps)
        new_file.save()
        for object in file_data["objects"]:
            new_bbox=Bbox.objects.create(xmin=object["xmin"],ymin=object["ymin"],xmax=object["xmax"],ymax=object["ymax"])
            new_bbox.save()
            serializer1=BboxSerializer(new_bbox)
            new_pol=Polygon.objects.create(ref="ref")
            new_pol.save()
            for p in object["polygon"]:
                new_point=Point.objects.create(x=p["x"],y=p["y"])
                new_point.save()
                serializer3=PointSerializer(new_point)
                new_pol.points.add(new_point)
            serializer2=PointSerializer(new_pol)
            new_object=Object.objects.create(str=object["str"],polygon=new_pol,bbox=new_bbox)
            new_object.save()
            serializer4=ObjectSerializer(new_object)
            new_file.objets.add(new_object)
        serializer=FileSerializer(new_file)
        return Response(serializer.data)

class Gps_locaViewSet(viewsets.ModelViewSet):
    serializer_class=Gps_locaSerializer

    def get_queryset(self):
        gpses=Gps_loca.objects.all()
        return gpses

class PointViewSet(viewsets.ModelViewSet):
    serializer_class=PointSerializer    
    def get_queryset(self):
        points=Point.objects.all()
        return points
   
class PolygonViewSet(viewsets.ModelViewSet):
    serializer_class=PolygonSerializer

    def get_queryset(self):
        polygons=Polygon.objects.all()
        return polygons


class BboxViewSet(viewsets.ModelViewSet):
    serializer_class=BboxSerializer

    def get_queryset(self):
        bboxs=Bbox.objects.all()
        return bboxs

class ObjectViewSet(viewsets.ModelViewSet):
    serializer_class=ObjectSerializer
    
    def get_queryset(self):
        objects=Object.objects.all()
        return objects
    def create(self, request, *args, **kwargs):
        object_data=request.data
        
        if object_data["pol"] != "":
            new_bbox=Bbox.objects.create(xmin=object_data["xmin"],ymin=object_data["ymin"],xmax=object_data["xmax"],ymax=object_data["ymax"])
            new_bbox.save()
            serializer1=BboxSerializer(new_bbox)
            new_object=Object.objects.create(str=object_data["str"],polygon=Polygon.objects.filter(ref=object_data["pol"]).get(),bbox=new_bbox)
            new_object.save()
        else:      
            new_pol=Polygon.objects.create(ref=object_data["ref"])
            new_pol.save()
            serializer2=PolygonSerializer(new_pol) 
            new_bbox=Bbox.objects.create(xmin=object_data["xmin"],ymin=object_data["ymin"],xmax=object_data["xmax"],ymax=object_data["ymax"])
            new_bbox.save()
            serializer1=BboxSerializer(new_bbox)
            new_object=Object.objects.create(str=object_data["str"],polygon=new_pol,bbox=new_bbox) 
            new_object.save()
        serializer=ObjectSerializer(new_object)
        return Response(object_data)


