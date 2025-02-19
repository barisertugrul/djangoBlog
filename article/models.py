"""
Article App Models
"""
from django.db import models

# Create your models here.

class Article(models.Model):
    """Article Model"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar')
    title = models.CharField(max_length=120, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')

    def __str__(self):
        """String representation of the model"""
        return self.title + ' (' + self.author.username  + ')'
