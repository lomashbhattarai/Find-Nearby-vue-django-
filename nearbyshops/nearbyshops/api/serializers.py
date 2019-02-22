from django.contrib.auth.models import User,Group
from rest_framework import serializers
from shops.models import Hospital
import re

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields =('url','username','email','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Group
        fields= ('url','name')

class HospitalSerializer(serializers.ModelSerializer):
    location =serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields= '__all__'
    
    def get_location(self,obj):
        return str(obj.location)
