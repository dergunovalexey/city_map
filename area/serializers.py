from rest_framework.serializers import ModelSerializer
from area.models import MicroArea


class MicroAreaSerializer(ModelSerializer):
    class Meta:
        model = MicroArea
        fields = ('__all__', )
        readonly_fields = ('__all__', )
