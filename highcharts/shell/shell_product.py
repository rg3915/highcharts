import csv
from highcharts.core.models import Product, Category

product_list = []

''' Lendo os dados de product.csv '''
with open('highcharts/fix/product.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        product_list.append(dct)
    f.close()


for i in product_list:
    category = Category.objects.get(category=i['category'])
    obj = Product.objects.create(
        category=category,
        product=i['product'],
        price=float(i['price']),
    )


# done
