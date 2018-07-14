from rest_framework.serializers import ModelSerializer
from complaint.models import Complaint


class ComplaintSerializer(ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'user', 'title', 'description',
                  'photo', 'status', 'updated_at', 'created_at')
        read_only_fields = ('id', 'status', 'updated_at', 'created_at')
        write_only_fields = ('user', )

    def create(self, validated_data):
        request = self.context['request']
        validated_data['user'] = request.user
        return super().create(validated_data)
