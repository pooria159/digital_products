from rest_framework import serializers

from .models import Category , File , Product



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title' , 'description' , 'avatar')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id','title' , 'file' , 'file_type')


# Method 1 

# class ProductSerializer(serializers.ModelSerializer):
    
#     categories = CategorySerializer(many=True)
#     files = FileSerializer(many=True)

#     class Meta:
#         model = Product
#         fields = ('id','title' , 'description' , 'avatar' , 'categories' , 'files')

# Method 2

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    categories = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title' , 'description' , 'avatar' , 'categories' , 'files' , 'url')