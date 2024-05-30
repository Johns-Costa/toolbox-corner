from django.contrib import admin
from .models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'stars', 'created_at')
    list_filter = ('stars', 'created_at')
    search_fields = ('content',)
