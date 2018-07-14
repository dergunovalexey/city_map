from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from complaint.models import Complaint
from complaint.serializers import ComplaintSerializer


class ComplaintViews(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
