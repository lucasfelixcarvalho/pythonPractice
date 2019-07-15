from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='New Title', widget=forms.TextInput(
        attrs={
            "placeholder": "Inform new title"
        }
    ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": 15,
            "cols": 30,
            "placeholder": "Inform new description"
        }
    ))
    price = forms.DecimalField(initial=99.99)
