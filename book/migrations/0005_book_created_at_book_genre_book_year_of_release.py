# Generated by Django 5.0.2 on 2024-02-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-02-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='year_of_release',
            field=models.DateField(default='2015-01-21'),
            preserve_default=False,
        ),
    ]
