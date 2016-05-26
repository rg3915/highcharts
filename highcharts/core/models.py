from django.db import models
from django.utils.formats import number_format


class Dollar(models.Model):
    date = models.DateField('data')
    value = models.DecimalField('valor', max_digits=4, decimal_places=3)

    class Meta:
        ordering = ['date']
        verbose_name = 'dólar'
        verbose_name_plural = 'dólares'

    def __str__(self):
        return self.value


class Euro(models.Model):
    date = models.DateField('data')
    value = models.DecimalField('valor', max_digits=4, decimal_places=3)

    class Meta:
        ordering = ['date']
        verbose_name = 'euro'
        verbose_name_plural = 'euros'

    def __str__(self):
        return self.value


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em', auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        'modificado em', auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Customer(models.Model):
    name = models.CharField('nome', max_length=50, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.name


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

    def get_price(self):
        return "R$ %s" % number_format(self.price, 2)

    def get_ipi(self):
        return "%s" % number_format(self.ipi * 100, 0)


class Sale(TimeStampedModel):
    customer = models.ForeignKey('Customer', verbose_name='cliente')

    class Meta:
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __str__(self):
        return str(self.id)

    def get_detalhe(self):
        return u"/sale/%i" % self.id


class SaleDetail(models.Model):
    sale = models.ForeignKey('Sale', verbose_name='venda')
    product = models.ForeignKey('Product', verbose_name='produto')
    quantity = models.PositiveSmallIntegerField('quantidade')
    price_sale = models.DecimalField(
        'preço de venda', max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return str(self.sale)

    def price_sale_formated(self):
        return "R$ %s" % number_format(self.price_sale, 2)
