from rest_framework.serializers import ModelSerializer
from complaint.models import Complaint


class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'title', 'description',
                  'status', 'updated_at', 'created_at')
        read_only_fields = ('id', 'status', 'updated_at', 'created_at')
