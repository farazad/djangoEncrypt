# urls.py
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', obtain_jwt_token, name='token-obtain-pair'),
    path('refresh-token/', refresh_jwt_token, name='token-refresh'),
    path('verify-token/', verify_jwt_token, name='token-verify'),
]
