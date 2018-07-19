from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from trackrecorder.serializers import RoadTrackSerializer


class RoadTrackViews(CreateModelMixin, GenericViewSet):
    serializer_class = RoadTrackSerializer
