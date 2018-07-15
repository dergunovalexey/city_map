from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from citizen.models import Citizen
from citizen.serializers import CitizenSerializer


class CitizenViews(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
