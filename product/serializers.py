import re
from datetime import datetime
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'created')
        
        
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be less than zero.")
        return value
    
    def validate_title(self, value):
        if re.search(r'[^\w\s]', value):
            raise serializers.ValidationError("Title cannot contain special characters.")
        return value
    
    def create(self, validated_data):
        product = Product(creator=self.context.get('user'),created=datetime.now(), **validated_data)
        product.save()
        return product