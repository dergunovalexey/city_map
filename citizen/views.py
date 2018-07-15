from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                   RetrieveModelMixin)
from citizen.models import Citizen
from citizen.serializers import CitizenSerializer


class CitizenViews(ListModelMixin, CreateModelMixin,
                   RetrieveModelMixin, GenericViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer
