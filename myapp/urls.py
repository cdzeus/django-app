from django.contrib import admin
from django.urls import path
from .views import ma_page

urlpatterns = [
    path('ma_page/', ma_page, name='ma_page'),
]
