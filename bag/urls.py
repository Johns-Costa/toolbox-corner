from django.urls import path
from .views import add_to_bag, view_bag, remove_from_bag

urlpatterns = [
    path('add/<int:product_id>/', add_to_bag, name='add_to_bag'),
    path('', view_bag, name='view_bag'),
    path('remove/<int:product_id>/', remove_from_bag, name='remove_from_bag'),
]