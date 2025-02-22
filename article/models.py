"""
Article App Models
"""
from django.db import models

# Create your models here.

class Article(models.Model):
    """Article Model"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=120, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    def __str__(self):
        """String representation of the model"""
        return self.title + ' (' + self.author.username  + ')'
