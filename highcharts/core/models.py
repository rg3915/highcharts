from django.db import models


class Dollar(models.Model):
    date = models.DateField('data')
    value = models.DecimalField('valor', max_digits=4, decimal_places=3)

    class Meta:
        ordering = ['date']
        verbose_name = 'dólar'
        verbose_name_plural = 'dólares'

    def __str__(self):
        return str(self.value)


class Euro(models.Model):
    date = models.DateField('data')
    value = models.DecimalField('valor', max_digits=4, decimal_places=3)

    class Meta:
        ordering = ['date']
        verbose_name = 'euro'
        verbose_name_plural = 'euros'

    def __str__(self):
        return str(self.value)


class Category(models.Model):
    category = models.CharField('categoria', max_length=50, unique=True)

    class Meta:
        ordering = ['category']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.category


class Product(models.Model):
    category = models.ForeignKey('Category', verbose_name='categoria')
    product = models.CharField('Produto', max_length=60, unique=True)
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['product']
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.product
