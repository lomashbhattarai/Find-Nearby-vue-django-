from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import WorldBorder

@admin.register(WorldBorder)
class WorldBorderAdmin(OSMGeoAdmin):
    list_display =('name','area')


# Register your models here.
