
from rest_framework import serializers

from referral.serializers import ReferrerSerializer
from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):

    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'access_token', 'refresh_token')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'referral_date_joined')

class CurrentUserSerializer(serializers.ModelSerializer):
    referrer_data = ReferrerSerializer(read_only=True)
    referrer_user = UserSerializer(read_only=True)
    referrals = UserSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'referrer_data', 'referral_date_joined', 'referrer_user', 'referrals')


class UserDetailSerializer(serializers.ModelSerializer):
    referrer_data = ReferrerSerializer(read_only=True)
    referrals = UserSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'referrer_data', 'referrals')


