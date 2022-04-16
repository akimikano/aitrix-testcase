from django.contrib import admin
from django.urls import path
from applications.core.views import CategoryView, SubcategoryView, ItemView

urlpatterns = [
    path('categories/', CategoryView.as_view({'get': 'list'})),

    path('subcategories/', SubcategoryView.as_view({'get': 'list'})),
    path('subcategories/<int:pk>/', SubcategoryView.as_view({'get': 'retrieve'})),

    path('items/', ItemView.as_view({'get': 'list'})),
]