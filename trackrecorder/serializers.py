from rest_framework import serializers
from trackrecorder.models import RoadTreck


class RoadTrackSerializer(serializers.ModelSerializer):
    default_error_messages = {
        'incorrect': 'incorrect points',
        'incorrect_type_content': 'incorrect values type',
        'incorrect_type_field': 'incorrect data type into field',
    }

    class Meta:
        model = RoadTreck
        fields = ('start', 'end', 'accselerometer_points',
                  'magnetometer_points')

    def val_poins(self, attr):
        if not isinstance(attr, dict):
            self.fail('incorrect_type_field')

        lat = attr.get('lat')
        lng = attr.get('lng')
        timst = attr.get('timestamp')

        checks = (lat, lng, timst)

        if not all(list(map(lambda x: isinstance(x, float), checks))):
            self.fail('incorrect_type_content')

        return attr

    def val_sensor_signal(self, attr):
        if not isinstance(attr, list):
            self.fail('incorrect_type_field')

        for a in attr:
            if not isinstance(a, dict):
                self.fail('incorrect_type_field')

            timst = a.get('timestamp')
            x = a.get('X')
            y = a.get('Y')
            z = a.get('Z')

            checks = (x, y, z, timst)

            if not all(list(map(lambda x: isinstance(x, float), checks))):
                self.fail('incorrect_type_content')

        return attr

    def validate_start(self, attr):
        attr = self.val_poins(attr)
        return attr

    def validate_end(self, attr):
        attr = self.val_poins(attr)
        return attr

    def validate_accselerometer_points(self, attr):
        attr = self.val_sensor_signal(attr)
        return attr

    def validate_magnetometer_points(self, attr):
        attr = self.val_sensor_signal(attr)
        return attr
