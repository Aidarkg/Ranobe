from django.contrib import admin
from book import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(models.Genre)
admin.site.register(models.BookFile)