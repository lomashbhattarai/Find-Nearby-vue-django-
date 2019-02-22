from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Shop,RoadSegment,Hospital
from django.contrib.gis.geos import GEOSGeometry,LineString,Point
from django.contrib.gis.geos import fromfile


longitude = 85
latitude =27

point= Point(longitude,latitude,srid=4326)
line = LineString((0, 0), (0, 50), (50, 50), (50, 0), (0, 0),srid=4326)

pnt = GEOSGeometry('SRID=4326;POINT(40.396764 -3.68042)')
pnt2 = GEOSGeometry('SRID=4326;POINT( {} {}  )'.format(line[1][0],line[1][1]))

print("lomash")
print(pnt)
print(pnt2)
print(pnt.distance(pnt2) * 100)
print("check")
print(line.distance(pnt))

user_location =GEOSGeometry('POINT({} {})'.format(latitude, longitude), srid=4326)

# user_location = POINT(longitude,latitude,srid=4326)
# Create your views here.

class Home(generic.ListView):
    model= Shop
    context_object_name ='shops'
    queryset = Shop.objects.annotate(distance= Distance('location',user_location)).order_by('distance')[0:20]
    template_name ='home.html'


def Road(request):
    road_0= RoadSegment.objects.all() 
    road = RoadSegment.objects.all()
    [line.geom.transform(3857) for line in road]
    
    return render(request,'road.html',{'road':road,'road_0':road_0})


def RoadUnit(request,id):
    road = RoadSegment.objects.all().get(pk=id)
    print(road)
    shops = [(x.name,road.geom.distance(x.location)) for x in Shop.objects.all()]
    print(shops)

    return render(request,'roadunit.html',{'name':road.segment,'shops':shops})

class Hospital(generic.ListView):
    model=Hospital
    context_object_name='hospitals'
    queryset= Hospital.objects.all()
    template_name='hospital.html'