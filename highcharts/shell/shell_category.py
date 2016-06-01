import csv
from highcharts.core.models import Category

category_list = []

''' Lendo os dados de category.csv '''
with open('highcharts/fix/category.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        category_list.append(dct)
    f.close()


obj = [Category(category=val['category']) for val in category_list]
Category.objects.bulk_create(obj)


# done
