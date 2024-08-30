from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class ProductListView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True , context={'request' : request})
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, context={'request': request})
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
        
class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories , many=True , context={'request' : request})
        return Response(serializer.data)

class CategoryDetailView(APIView):
    
    def get(self, request , pk):
        try:
            categories = Category.objects.get(pk=pk)
            serializer = CategorySerializer(categories , context={'request' : request})
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"error" : "Category not found"} , status=404)


class FileListView(APIView):
    def get(self , request , product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files , many=True , context={'request' : request})
        return Response(serializer.data)
    

class FileDetailView(APIView): 
    def get(self , request , product_id , pk):
        try:
            f = File.objects.get(pk=pk , product_id=product_id)
            serializer = FileSerializer(f , context={'request' : request})
            return Response(serializer.data)
        except File.DoesNotExist:
            return Response({"error" : "File not found"} , status=404)


    