"""
Article App Models
"""
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    """Article Model"""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=120, verbose_name='Title')
    content = RichTextField(verbose_name='Content')
    article_image = models.FileField(null=True, blank=True, verbose_name='Article Image')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    class Meta:
        """Meta definition for Article."""
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created_date']

    def __str__(self):
        """String representation of the model"""
        return self.title + ' (' + self.author.username  + ')'


class Comment(models.Model):
    """Comment Model"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Article')
    comment_author = models.CharField(max_length=50, verbose_name='Name')
    comment_content = models.TextField(verbose_name='Content')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Comment Date')

    class Meta:
        """Meta definition for Comment."""
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_date']

    def __str__(self):
        """String representation of the model"""
        return self.comment_content
