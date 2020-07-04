# from django.db import models
from django.contrib.gis.db import models

class Point(models.Model):
    """A single GDELT event point"""
    geometry = models.PointField(srid=4326)

