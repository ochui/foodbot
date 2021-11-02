from djmoney.models.fields import MoneyField
from django.db import models


class Ingredient(models.Model):

    name = models.CharField(max_length=150)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency='GBP')

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredient'

    def __str__(self):
        return self.name


class Food(models.Model):

    name = models.CharField(max_length=200)
    cooking_time = models.CharField(max_length=150)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'
