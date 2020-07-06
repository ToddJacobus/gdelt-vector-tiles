from rest_framework import viewsets, mixins, generics

from core.models import Point
from point.serializers import PointSerializer


class PointViewSet(viewsets.GenericViewSet,
                   mixins.CreateModelMixin,
                  ):

    serializer_class = PointSerializer
    queryset = Point.objects.all()

    def perform_create(self, serializer):
        """create a new Point"""
        data = serializer.validated_data

        import pdb; pdb.set_trace()

        serializer.save(**data)
