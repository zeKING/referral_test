from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers

from referal_project.exceptions import WrongDateException, CodeExistsException, AlreadyReferralException, \
    SelfReferrerException, AlreadyReferrerException, ReferrerExpiredException
from referral.models import Referrer
from users.models import User


class ReferrerSerializer(serializers.ModelSerializer):

    code = serializers.CharField()

    class Meta:
        model = Referrer
        fields = ['code', 'deadline']

    def create(self, validated_data):

        user = self.context['request'].user
        if Referrer.objects.filter(user_id=user.id).exists():
            raise AlreadyReferrerException

        code = validated_data.get('code')
        if Referrer.objects.filter(code=code).exists():
            raise CodeExistsException

        deadline = validated_data.get('deadline')
        if deadline < timezone.now():
            raise WrongDateException

        referrer = Referrer(**validated_data)
        referrer.user = user

        referrer.save()
        return referrer


class ReferralCreateSerializer(serializers.ModelSerializer):

    code = serializers.CharField(write_only=True)
    referral_date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ['code', 'referral_date_joined']

    def create(self, validated_data):

        code = validated_data.get('code')

        referrer_data = get_object_or_404(Referrer, code=code)

        user = self.context['request'].user
        if user.referrer_user is not None:
            raise AlreadyReferralException

        if user.id == referrer_data.user_id:
            raise SelfReferrerException

        if referrer_data.deadline < timezone.now():
            raise ReferrerExpiredException

        user.referrer_user = referrer_data.user
        user.referral_date_joined = timezone.now()

        user.save()
        return user


# class ReferralSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Referral
#         fields = ['date_joined']