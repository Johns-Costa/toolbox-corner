from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for the Contact model."""

    list_display = ('subject', 'email', 'content', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('email', 'content')