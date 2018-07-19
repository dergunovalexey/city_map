from rest_framework import serializers
from area.models import MicroArea


class MicroAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroArea
        fields = ('id', 'latitude_left', 'longitude_left', 'latitude_right',
                  'longitude_right', 'level')
        read_only_fields = ('id', 'latitude_left', 'longitude_left',
                            'latitude_right', 'longitude_right', 'level')


class Points(serializers.Serializer):
    latitude_first = serializers.FloatField()
    longitude_first = serializers.FloatField()
    latitude_second = serializers.FloatField()
    longitude_second = serializers.FloatField()
