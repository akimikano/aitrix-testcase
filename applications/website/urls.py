from django.contrib import admin
from django.urls import path
from applications.website.views import MainView

urlpatterns = [
    path('main/', MainView.as_view())
]