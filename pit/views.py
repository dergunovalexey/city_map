from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from pit.serializers import PitSerializer


class PitViews(CreateModelMixin, GenericViewSet):
    serializer_class = PitSerializer
    permission_classes = [IsAuthenticated]
