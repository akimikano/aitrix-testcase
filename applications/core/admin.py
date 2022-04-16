from django.contrib import admin
from applications.core.models import Category, Subcategory, Item

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Item)
