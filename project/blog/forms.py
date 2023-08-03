from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'photo',
            'is_published',
            'category',
            'author'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nomi'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Matni"
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'author': forms.Select(attrs={
                'class': 'form-select',
            }),
        }