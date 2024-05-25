from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import ProductSerializer
from .models import Product


class CreateProductView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ShowProductView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()