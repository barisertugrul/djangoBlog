# Generated by Django 5.1.6 on 2025-02-25 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_date',
            new_name='created_date',
        ),
    ]
