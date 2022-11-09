from django.db import models


class Hotel(models.Model):
    name = models.CharField('Название', max_length=50)
    country = models.CharField('Страна', max_length=50)
    stars = models.IntegerField('Звездность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
