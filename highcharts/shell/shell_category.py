import csv
from highcharts.core.models import Category

category_list = []

''' Lendo os dados de category.csv '''
with open('highcharts/fix/category.csv', 'r') as f:
    rows = csv.reader(f)
    for row in rows:
        category_list.append(row[0])
    f.close()


obj = [Category(category=val) for val in category_list]
Category.objects.bulk_create(obj)


# done
