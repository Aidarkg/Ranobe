# Generated by Django 5.0.2 on 2024-02-20 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ranobe_file',
            field=models.FileField(null=True, upload_to='media/ranobe'),
        ),
    ]
