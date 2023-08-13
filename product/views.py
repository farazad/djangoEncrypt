from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer

class ProductRegistrationView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={'user':request.user})
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product registered successfully"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)