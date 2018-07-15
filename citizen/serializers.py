from rest_framework.serializers import ModelSerializer
from citizen.models import Citizen


class CitizenSerializer(ModelSerializer):
    class Meta:
        model = Citizen
        fields = ('id', 'title', 'description', 'address', 'latitude',
                  'longitude', 'photo', 'status', 'updated_at', 'created_at')
        read_only_fields = ('id', 'status', 'photo', 'updated_at', 'created_at')
