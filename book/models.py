from django.db import models


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
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class BookFile(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/file')