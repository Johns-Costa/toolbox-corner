from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    Form to create or edit a review.
    """
    class Meta:
        """
        Meta class to specify the model and fields used in the form.
        """
        model = Review
        fields = ['content', 'stars']