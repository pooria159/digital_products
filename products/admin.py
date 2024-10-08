from django.contrib import admin
from .models import Category,File,Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent' , 'title', 'is_enable' , 'create_time']
    list_filter = ['is_enable' , 'parent']
    search_fields = ['title']

class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title' ,'file_type', 'file' , 'is_enable']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'is_enable' , 'create_time']
    list_filter = ['is_enable']
    filter_horizontal = ['categories']
    search_fields = ['title']
    inlines = [FileInlineAdmin]



