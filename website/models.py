from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """Model representing product categories."""
    class Meta:
        # Plural name for the admin interface
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        """String representation of the category."""
        return self.name


class Product(models.Model):
    """Model representing products."""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True,
                                   on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,
                                 null=True, blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='products')

    def __str__(self):
        """String representation of the product."""
        return self.name


class ProductImage(models.Model):
    """Model representing product images."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')
    image = CloudinaryField('image', default='placeholder')
    alt = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """String representation of the product image."""
        return f"Image for {self.product.name}"
