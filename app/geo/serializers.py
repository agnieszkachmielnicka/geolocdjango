from geo.models import GeoLocation
from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField

class GeoLocationSerializer(serializers.ModelSerializer):
    geo_location = PointField()
    
    class Meta:
        model = GeoLocation
        fields = ['id','geo_location']