from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """Form for contacting purposes."""

    class Meta:
        model = Contact
        fields = ['subject', 'content', 'email']
