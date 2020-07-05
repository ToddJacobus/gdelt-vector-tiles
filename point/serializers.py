from rest_framework import serializers

from core.models import Point


class PointSerializer(serializers.ModelSerializer):
    """Serializer for Point object"""

    class Meta:
        model = Point
        fields ='__all__'