"""
Article Admin
"""
from django.contrib import admin

from .models import Article, Comment


# Register your models here.

admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Article Admin"""

    list_display = ['title', 'author', 'created_date']
    list_display_links = ['title', 'created_date']
    search_fields = ['title', 'author__username']
    list_filter = ['created_date', 'author']
    class Meta:
        model = Article
