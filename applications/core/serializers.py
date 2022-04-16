from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from applications.core.models import Category, Subcategory, Item


class SubcategorySerializer(ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'category', 'category_name')


class CategorySerializer(ModelSerializer):
    subcategories = SubcategorySerializer(many=True, source='subcategory_set')

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')


class ItemSerializer(ModelSerializer):
    subcategory_name = serializers.CharField(source='subcategory.name')

    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'subcategory', 'subcategory_name')