from django.contrib import admin
from user import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_links = ('id', 'user')


@admin.register(models.SMSCode)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'code')

