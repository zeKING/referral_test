from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from users.models import User
from users.serializers import UserCreateSerializer, CurrentUserSerializer


# Create your views here.


class RegisterAPIView(CreateAPIView):

    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        user = User.objects.get(id=response.data['id'])
        response.data['access'] = str(AccessToken.for_user(user))
        response.data['refresh'] = str(RefreshToken.for_user(user))

        return response

class CurrentUserAPIView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    serializer_class = CurrentUserSerializer


