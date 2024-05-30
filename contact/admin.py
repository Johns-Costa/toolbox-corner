from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'content', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('email', 'content')