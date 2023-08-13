# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    username = serializers.CharField(max_length=150)  # Adjust max_length as needed
    
    class Meta:
        model = User
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
