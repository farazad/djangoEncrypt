from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),  # Obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),  # Refresh JWT token
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),  # Verify JWT token
]
