from django.db import models
from ebooklib import epub
from django.core.exceptions import ValidationError


class Book(models.Model):
    title = models.CharField(max_length = 50)
    photo = models.ImageField(upload_to='media/photo', null=False)
    author = models.CharField(max_length = 50)
    description = models.TextField()
    year_of_release = models.DecimalField(max_digits=4, decimal_places=0)
    genre = models.ManyToManyField(
        'Genre',
        related_name='genres',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length = 100, unique = True, verbose_name ='название')

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class BookFile(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/file')


class Book2(models.Model):
    photo = models.ImageField(upload_to='media/photo', verbose_name='фото', unique=True)
    file = models.FileField(upload_to='media/file', verbose_name="файл", unique=True)
    years_of_release = models.CharField(max_length=10, verbose_name='год релиза')
    title = models.CharField(max_length=255, editable=False, verbose_name='название', unique=True)
    author = models.CharField(max_length = 50, editable=False, verbose_name='автор')
    description = models.TextField(editable=False, verbose_name='описание')

    def save(self):
        try:
            super().save()

            book_file_path = self.file.path

            book = epub.read_epub(book_file_path)

            self.title = book.get_metadata("DC", "title")[0][0]
            self.author = book.get_metadata("DC", "creator")[0][0]
            self.description = book.get_metadata("DC", "description")[0][0]
        except (IndexError, epub.EpubException, ValidationError):
            self.title = "Unknown Title"
            self.author = "Unknown Author"
            self.description = "Unknown Description"
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'