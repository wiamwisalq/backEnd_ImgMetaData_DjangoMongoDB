from django.urls import re_path,include
from django.db import router
from  .views import BboxViewSet, FileViewSet,Gps_locaViewSet,PointViewSet,PolygonViewSet,ObjectViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("file",FileViewSet,basename="file")
router.register("Gps_loca",Gps_locaViewSet,basename="Gps_loca")
router.register("polygons",PolygonViewSet,basename="polygons")
router.register("point",PointViewSet,basename="point")
router.register("object",ObjectViewSet,basename="object")
router.register("bbox",BboxViewSet,basename="bbox")
urlpatterns=[
    re_path('', include(router.urls))
]