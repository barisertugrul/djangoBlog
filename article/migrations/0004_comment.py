# Generated by Django 5.1.6 on 2025-02-25 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='Name')),
                ('comment_content', models.TextField(verbose_name='Content')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Comment Date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article', verbose_name='Article')),
            ],
        ),
    ]
