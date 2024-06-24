from django import forms
from .models import Product, ProductImage, Category
from django.forms import modelformset_factory


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.
    """
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'has_sizes', 'category']


class ProductImageForm(forms.ModelForm):
    """
    Form for creating and updating ProductImage instances.
    """
    class Meta:
        model = ProductImage
        fields = ['image', 'alt']

# Define the formset for ProductImage


ProductImageFormSet = modelformset_factory(ProductImage,
                                           form=ProductImageForm,
                                           extra=1, can_delete=True)
