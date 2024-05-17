from django import forms

class AddToBagForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)