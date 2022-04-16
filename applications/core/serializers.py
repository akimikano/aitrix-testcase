from rest_framework.serializers import ModelSerializer
from applications.core.models import Category, Subcategory, Item


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'category')


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'price', 'subcategory')