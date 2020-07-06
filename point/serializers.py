from rest_framework import serializers
from django.contrib.gis.geos import Point
from rest_framework_gis.serializers import GeometryField
# from rest_framework_gis.serializers import GeoFeatureModelSerializer

from core.models import Point


# class PointSerializer(serializers.ModelSerializer):
#     """Serializer for Point object"""

#     class Meta:
#         model = Point
#         fields ='__all__'

class PointSerializer(serializers.Serializer):
    """Serializer for Point object"""
    geometry = GeometryField()

