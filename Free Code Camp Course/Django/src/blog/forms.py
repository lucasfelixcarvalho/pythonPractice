from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={
            "placeholder": "Inform new title"
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "rows": 10,
            "cols": 50,
            "placeholder": "Inform new description"
        }
    ))