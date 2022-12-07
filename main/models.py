from django.db import models


class Country(models.Model):
    country = models.CharField('Страна', max_length=50)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Hotel(models.Model):
    name = models.CharField('Название', max_length=50)
    stars = models.IntegerField('Звездность')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
