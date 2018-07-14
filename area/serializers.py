from rest_framework.serializers import ModelSerializer
from area.models import MicroArea


class MicroAreaSerializer(ModelSerializer):
    class Meta:
        model = MicroArea
        fields = ('id', 'latitude_left', 'longitude_left', 'latitude_right',
                  'longitude_right', 'level')
        read_only_fields = ('id', 'latitude_left', 'longitude_left',
                          'latitude_right', 'longitude_right', 'level')
