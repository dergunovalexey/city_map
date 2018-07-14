from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from userdata.serializers import UserSerializer


class RegisterUser(GenericViewSet):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serialaizer = self.get_serializer(data=request.data)
        user = serialaizer.create()
        return Response(data=user)
