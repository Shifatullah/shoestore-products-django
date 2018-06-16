from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ListProductsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #queryset = Product.objects.all()
    productList = []
    productList.append(Product("iPhone 8",))
    productList.append(Product("iPhone X",))
    productList.append(Product("iPhone 7",))
    queryset = productList
    serializer_class = ProductSerializer

