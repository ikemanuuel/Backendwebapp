# views.py
from rest_framework import generics
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class CategoryViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemViewSet(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
