from rest_framework import serializers
import re
from userdata.models import User
import string
import random


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

    def create(self, session):
        self.is_valid(raise_exception=True)
        phone = self.data['phone']

        code = ''.join(
            random.choice(string.digits) for _ in range(self.CODE_LENGTH))

        session['code_verification'] = code
        session['phone'] = phone


class CodeSerializer(serializers.Serializer):
    default_error_messages = {
        "incorrect_code": "Неверный код"
    }

    CODE_LENGTH = 6

    code = serializers.CharField(max_length=CODE_LENGTH)

    def validate_code(self, attr):

        result = re.match(r"^\d{%d}$" % self.CODE_LENGTH, self.code)

        if not result:
            self.fail('incorrect_code')

        if self.code != self.context['code']:
            self.fail('incorrect_code')

        return attr

    def create(self, session):
        phone = session['phone']
        User.objects.create(username=phone, phone=phone)
