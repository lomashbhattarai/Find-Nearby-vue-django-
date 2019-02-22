from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop,RoadSegment,Hospital

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display =('name','location')

@admin.register(RoadSegment)
class RoadSegmentAdmin(OSMGeoAdmin):
    list_display =('segment','srftpe')

@admin.register(Hospital)
class HospitalAdmin(OSMGeoAdmin):
    list_display=('name','location')

# Register your models here.

