from django.contrib import admin
from book import models


@admin.register(models.Book2)
class Book2(admin.ModelAdmin):
    list_display = ('id', 'title', 'years_of_release')
    list_display_links = ('id', 'title', 'years_of_release')

    fields = ('id', 'title', 'description', 'photo', 'file', 'years_of_release')
    readonly_fields = ('id', 'title', 'description')


admin.site.register(models.Genre)