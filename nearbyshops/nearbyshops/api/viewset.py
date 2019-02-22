from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from nearbyshops.api.serializers import UserSerializer,GroupSerializer,HospitalSerializer
from shops.models import Hospital
from django.contrib.gis.db.models.functions import Distance
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.contrib.gis.geos import GEOSGeometry,LineString,Point


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class= UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset= Group.objects.all()
    serializer_class= GroupSerializer

class HospitalViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class= HospitalSerializer
    def get_serializer_context(self):
        return {'lat': self.kwargs['lat'],'long':self.kwargs['long']}
    def get_queryset(self, *args, **kwargs):
        longitude = self.kwargs['long']
        latitude =self.kwargs['lat']
        user_location =GEOSGeometry('POINT({} {})'.format(longitude,latitude), srid=4326)
        data={}
        queryset= Hospital.objects.all().annotate(distance= Distance('location',user_location)).order_by('distance')
        return queryset