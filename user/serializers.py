from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    username = serializers.CharField(max_length=150)  # Adjust max_length as needed
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
        
    def validate_username(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Username must contain only alphabetic characters.")
        return value
    
    def validate_password(self, value):
        if not any(char.isalpha() for char in value):
            raise serializers.ValidationError("Password must contain at least one alphabetic character.")
        
        if not any(char in value for char in ['#', '!']):
            raise serializers.ValidationError("Password must contain at least one '#' or '!' character.")
        
        return value
    
    def save(self):
        user_model = get_user_model()
        user = user_model(username=self.validated_data['username'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username

        return token