from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserRegistrationSerializer


class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        refresh = RefreshToken.for_user(user)
        data = serializer.data
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
