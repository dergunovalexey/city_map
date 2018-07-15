from rest_framework.serializers import ModelSerializer
from complaint.models import Complaint


class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'title', 'description', 'latitude', 'longitude',
                  'photo', 'status', 'updated_at', 'created_at')
        read_only_fields = ('id', 'status', 'photo', 'updated_at', 'created_at')
