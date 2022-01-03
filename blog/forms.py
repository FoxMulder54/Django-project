from django.db.models import fields
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["state"]

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }
