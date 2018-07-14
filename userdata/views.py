from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from userdata.serializers import UserSerializer, CodeSerializer


class SendRegistrationUserCodeView(GenericViewSet):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.create()
        return Response(status=200)


class CodeVerificationView(GenericViewSet):
    serializer_class = CodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'code': request.session['code_verification']})
        serializer.create(request.session)
        return Response(status=201)
