# Generated by Django 5.0.2 on 2024-03-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_book2_author_book2_description_book2_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book2',
            name='author',
            field=models.CharField(editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='book2',
            name='description',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='book2',
            name='title',
            field=models.CharField(editable=False, max_length=255),
        ),
    ]