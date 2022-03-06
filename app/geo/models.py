from django.contrib.gis.db import models

class GeoLocation(models.Model):
    geo_location = models.PointField()
    ip_url = models.CharField(max_length=500, blank=True, default='')