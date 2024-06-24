from django.db import models
from django.conf import settings
from website.models import Product


class Review(models.Model):
    """
    Model to represent a product review.
    """
    STAR_CHOICES = [(i, str(i)) for i in range(6)]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(max_length=500, blank=True)
    stars = models.IntegerField(choices=STAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class to enforce unique reviews per product-user pair.
        """
        unique_together = ('product', 'user')

    def __str__(self):
        """
        String representation of the review.
        """
        return f'Review for {self.product.name} by {self.user.username}'
        