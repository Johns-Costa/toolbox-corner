from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin configuration for the Review model."""

    list_display = ('product', 'user', 'stars', 'created_at')
    list_filter = ('stars', 'created_at')
    search_fields = ('content',)
