from django.db import models
from django.conf import settings
from website.models import Product 

# Create your models here.

class Review(models.Model):
    STAR_CHOICES = [(i, str(i)) for i in range(6)]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, blank=True)
    stars = models.IntegerField(choices=STAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'
