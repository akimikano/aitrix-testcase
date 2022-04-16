from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=128)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    category = models.ForeignKey(Category, models.CASCADE, verbose_name='Категория')
    name = models.CharField('Название', max_length=128)

    def __str__(self):
        return self.name


class Item(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    subcategory = models.ForeignKey(Subcategory, models.CASCADE, verbose_name='Подкатегория')
    name = models.CharField('Название', max_length=128)
    price = models.PositiveIntegerField('Цена')

    def __str__(self):
        return self.name
