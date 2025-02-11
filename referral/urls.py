from django.urls import path

from referral.views import (CreateReferrerAPIView, DeleteReferrerAPIView, RegisterReferralAPIView, ReferrerGetAPIView,
                            ReferrerGetByEmailAPIView)

urlpatterns = [
    path('code/create/', CreateReferrerAPIView.as_view()),
    path('code/delete/', DeleteReferrerAPIView.as_view()),
    path('create/', RegisterReferralAPIView.as_view()),
    path('referrer/detail/<int:user_id>/', ReferrerGetAPIView.as_view()),
    path('referrer/detail-email/', ReferrerGetByEmailAPIView.as_view())
]