from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from area.serializers import MicroAreaSerializer
from area.choices import LevelDangerous
from area.models import MicroArea


class MicroAreaViews(ListModelMixin, GenericViewSet):
    queryset = MicroArea.objects.exclude(level=LevelDangerous.NOT)
    serializer_class = MicroAreaSerializer
