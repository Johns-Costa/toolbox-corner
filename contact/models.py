from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone

class Contact(models.Model):
    """Model to store contact form submissions."""
    SUBJECT_CHOICES = [
        ('problems', 'Problems'),
        ('product_info', 'Product Information'),
        ('general_info', 'General Information'),
        ('work_with_us', 'Work with Us'),
        ('other', 'Other'),
    ]

    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    content = models.TextField(validators=[MinLengthValidator(10), MaxLengthValidator(500)])
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_subject_display()} - {self.email}"
