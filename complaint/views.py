from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from complaint.models import Complaint
from complaint.serializers import ComplaintSerializer


class ComplaintViews(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Complaint.objects.filter(user=user
                                        ).order_by('-created_at')
