from django.db import models


class Categories(models.Model):
    title = models.CharField(verbose_name='Name', max_length=64)
    description = models.TextField('Description', max_length=255)
    price = models.DecimalField(decimal_places=2)

"""
Пример:

# title: название кофе
# id: уникальный идентификатор (задается автоматически)
# Описание объекта кофе (поля: id, название)


class Coffee(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Название'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Кофе'
        verbose_name_plural = 'Кофе'
        
class Price(models.Model):
    price = models.PositiveIntegerField(
        verbose_name = 'Цена'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

class Volume(models.Model):
    title = models.CharField(
        max_length=32,
        verbose_name='Объем'
    )
    
    price = models.OneToOneField(
        'Price',
        verbose_name='Цена кофе',
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Объём'
        verbose_name_plural = 'Объёмы'
        
class Topping(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='Сироп'
    )
    
    price = models.ForeignKey(
        'Price',
        verbose_name='Цена сиропа',
        on_delete=models.CASCADE
    )    
    
    def __str__(self):
    return self.title
        
    class Meta:
        verbose_name = 'Сироп'
        verbose_name_plural = 'Сиропы'

class Profile(models.Model):
    pass
    
class Order(models.Model):
    pass
    
"""

