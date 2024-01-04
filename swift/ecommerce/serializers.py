# serializers.py
from rest_framework import serializers
from .models import Category, Item

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        if obj.category:
            category = obj.category
            category_name = category.category_name
            return category_name
        return None
    class Meta:
        model = Item
        fields = '__all__'
