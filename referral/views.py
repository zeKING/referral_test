from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated


from referral.models import Referrer
from referral.serializers import ReferrerSerializer, ReferralCreateSerializer
from users.models import User
from users.serializers import  UserDetailSerializer


# Create your views here.

class CreateReferrerAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = ReferrerSerializer


class DeleteReferrerAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Referrer, user_id=self.request.user.id)


class RegisterReferralAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = ReferralCreateSerializer

    @swagger_auto_schema(operation_summary="Register as referral")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ReferrerGetAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_url_kwarg = 'user_id'

    @method_decorator(cache_page(10))
    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)


class ReferrerGetByEmailAPIView(RetrieveAPIView):
    email = openapi.Parameter('email', openapi.IN_QUERY, description='Email of referrer', required=True,
                              type=openapi.TYPE_STRING)

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_url_kwarg = 'email'
    lookup_field = 'email'

    def get_object(self):
        email = self.request.query_params.get('email', None)
        if email is None:
            raise serializers.ValidationError('Query parameter `email` is required')
        return get_object_or_404(User, email=email)

    @swagger_auto_schema(manual_parameters=[email], operation_summary="Get information about referrer")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
