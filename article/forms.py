from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    """Form for creating articles"""
    class Meta:
        model = Article
        fields = ['title', 'content', 'article_image']
        labels = {
            'title': 'Title',
            'content': 'Content',
            'article_image': 'Featured Image'
        }
