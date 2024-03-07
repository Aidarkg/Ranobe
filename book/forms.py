from django import forms
from book import models


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ('title', 'photo', 'author', 'description', 'year_of_release', 'genre')
        labels = {
            'title': 'Название',
            'photo': 'Фото',
            'author': 'Автор',
            'description': 'Описание',
            'year_of_release': 'Год релиза',
            'genre': 'Жанры'
        }
        