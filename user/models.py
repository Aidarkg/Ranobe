from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='пользователь')
    photo = models.ImageField(upload_to='media/photo', verbose_name='фото')
    phone = models.CharField(max_length=15, verbose_name='номер телефона')


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class SMSCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='code', verbose_name='пользователь')
    code = models.CharField(max_length=10, verbose_name='код')

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Коды'

    def __str__(self):
        return self.code