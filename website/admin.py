from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):
    """
    Defines the inline representation of ProductImage model in the admin interface.
    Allows adding/editing images directly in the Product admin page.
    """
    model = ProductImage 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Defines the admin interface for the Product model.
    """
    list_display = ('name', 'price', 'created_by', 'created_at') 
    list_filter = ('created_at',) 
    search_fields = ('name',)  
    inlines = [ProductImageInline] 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Defines the admin interface for the Category model.
    """
    list_display = ('name',)
