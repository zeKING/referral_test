from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegisterAPIView, CurrentUserAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('current-user/', CurrentUserAPIView.as_view())

]