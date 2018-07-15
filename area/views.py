from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from area.serializers import MicroAreaSerializer
from area.choices import LevelDangerous
from area.models import MicroArea


class MicroAreaViews(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = MicroArea.objects.exclude(level=LevelDangerous.NOT)
    serializer_class = MicroAreaSerializer
