from rest_framework import serializers
import re
from userdata.models import User
import string
import random
from rest_framework.authtoken.models import Token


CODE_LENGTH = 6


class UserSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)

    default_error_messages = {
        "incorrect_number": "Неверный формат номера"
    }

    def validate_phone(self, attr):
        result = re.match(r"^\+\d{11}$", attr)
        if not result:
            self.fail('incorrect_number')

        return attr

    def create(self):
        self.is_valid(raise_exception=True)
        phone = self.data['phone']

        code = ''.join(
            random.choice(string.digits) for _ in range(CODE_LENGTH))
        session = self.context['request'].session
        session['code'] = code
        session['phone'] = phone


class CodeSerializer(serializers.Serializer):
    default_error_messages = {
        "incorrect_code": "Неверный код"
    }

    code = serializers.CharField(max_length=CODE_LENGTH)

    def validate_code(self, attr):

        result = re.match(r"^\d{%d}$" % CODE_LENGTH, attr)

        if not result:
            self.fail('incorrect_code')

        if attr != self.context['request'].session['code']:
            self.fail('incorrect_code')

        return attr

    def create(self):
        self.is_valid(raise_exception=True)
        phone = self.context['request'].session['phone']
        user, created = User.objects.get_or_create(username=phone, phone=phone)
        token, created = Token.objects.get_or_create(user=user)
        return token.key
