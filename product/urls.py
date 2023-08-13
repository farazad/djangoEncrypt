from django.urls import path
from .views import ProductRegistrationView

urlpatterns = [
    path('register-product/', ProductRegistrationView.as_view(), name='product-registration'),
]