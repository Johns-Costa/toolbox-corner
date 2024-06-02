from django.urls import path
from . import views
from django.urls import path, include
from .views import edit_product, search_results

urlpatterns = [
    path('', views.home, name='home'),
    path('products/category/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('bag/', include('bag.urls')),
    path('search/', search_results, name='search_results'),
]
