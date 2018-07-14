from rest_framework import serializers
from pit.models import Pit


class PitSerializer(serializers.ModelSerializer):
    default_error_messages = {
        'not_positive_number_of_jolting': 'not positive number of jolting',
        'not_positive_speed': 'not positive speed',
    }

    class Meta:
        model = Pit
        fields = ('latitude', 'longitude', 'number_of_jolting', 'speed')

    def validate_number_of_jolting(self, attr):
        if attr <= 0:
            self.fail('not_positive_number_of_jolting')
        return attr

    def validate_speed(self, attr):
        if attr < 0:
            self.fail('not_positive_speed')
        return attr
