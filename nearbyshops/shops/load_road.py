import os
from django.contrib.gis.utils import LayerMapping
from .models import RoadSegment


roadsegment_mapping = {
    'ntlclass': 'ntlclass',
    'srftpe': 'srftpe',
    'segment': 'segment',
    'geom': 'LINESTRING',
}


road_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__),'data','road_segments.shp'),
)

def run(verbose=True):
    lm = LayerMapping(RoadSegment,road_shp,roadsegment_mapping,transform=False)
    lm.save(strict= True,verbose=verbose)

