from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from area.serializers import MicroAreaSerializer
from area.choices import LevelDangerous


class MicroAreaViews(ListModelMixin, GenericViewSet):
    serializer_class = MicroAreaSerializer

    def get_queryset(self):
        return super().get_queryset().exclude(level=LevelDangerous.NOT)
