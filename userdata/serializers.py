from rest_framework import serializers
import re
from userdata.models import User


class UserSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)

    default_error_messages = {
        "incorrect_number": "Неверный формат номера",
        "already_exists": "Номер уже зарегистрирован"
    }

    def validate_phone(self, attr):
        result = re.match(r"^\+\d{11}$", self.phone)
        if not result:
            self.fail('incorrect_number')

        if User.objects.filter(phone=attr).exists():
            self.fail('already_exists')

        return attr
