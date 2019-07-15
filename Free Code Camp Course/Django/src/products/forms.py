from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" not in title:
            raise forms.ValidationError("This is not a valid title")
        return title


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
