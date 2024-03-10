# Generated by Django 5.0.2 on 2024-03-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_alter_genre_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book2',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'жанр', 'verbose_name_plural': 'жанры'},
        ),
        migrations.AlterField(
            model_name='book2',
            name='author',
            field=models.CharField(editable=False, max_length=50, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='book2',
            name='description',
            field=models.TextField(editable=False, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='book2',
            name='file',
            field=models.FileField(upload_to='media/file', verbose_name='файл'),
        ),
        migrations.AlterField(
            model_name='book2',
            name='photo',
            field=models.ImageField(upload_to='media/photo', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='book2',
            name='title',
            field=models.CharField(editable=False, max_length=255, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='book2',
            name='years_of_release',
            field=models.CharField(max_length=10, verbose_name='год релиза'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='название'),
        ),
    ]