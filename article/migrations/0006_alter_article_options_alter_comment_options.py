# Generated by Django 5.1.6 on 2025-02-25 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_rename_comment_date_comment_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
