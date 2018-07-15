from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,
                                   RetrieveModelMixin)
from rest_framework.permissions import IsAuthenticated
from complaint.models import Complaint
from complaint.serializers import ComplaintSerializer


class ComplaintViews(ListModelMixin, CreateModelMixin,
                     RetrieveModelMixin, GenericViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     ii
    #     return Complaint.objects.filter(user=user
    #                                     ).order_by('-created_at')

    # def pre_save(self, obj):
    #     obj.photo = self.request.FILES.get('photo')
