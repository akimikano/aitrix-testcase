from rest_framework.viewsets import ModelViewSet
from applications.core.models import Category, Subcategory, Item
from applications.core.pagination import MainPagination
from applications.core.serializers import CategorySerializer, SubcategorySerializer, ItemSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.prefetch_related('subcategory_set').all()
    serializer_class = CategorySerializer


class SubcategoryView(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ItemView(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_fields = ('subcategory',)
    pagination_class = MainPagination


