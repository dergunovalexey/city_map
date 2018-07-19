from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from area.serializers import MicroAreaSerializer, Points
from area.choices import LevelDangerous
from area.models import MicroArea


class MicroAreaViews(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = MicroArea.objects.exclude(level=LevelDangerous.NOT)
    serializer_class = MicroAreaSerializer


class PointsViews(GenericViewSet):
    serializer_class = Points
    def create(self, request, *args, **kwargs):
        return Response(200)