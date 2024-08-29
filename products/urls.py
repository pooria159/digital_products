from django.contrib import admin
from django.urls import path
from .views import *

# name syntax : correct : name-example
# wrong : name_example , name@example , ....

urlpatterns = [
    path('products/' , ProductListView.as_view() , name='product-list'),
    path('products/<int:pk>/' , ProductDetailView.as_view() , name='product-detail'),
]