import csv
import datetime as dt
from highcharts.core.models import Dollar

dollar_list = []

''' Lendo os dados de dollar.csv '''
with open('highcharts/fix/dollar.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        # Convert '%d/%m/%Y' to '%Y-%m-%d'.
        d = dt.datetime.strptime(dct['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
        dollar_list.append((d, dct['value']))
    f.close()


obj = [Dollar(date=val[0], value=val[1]) for val in dollar_list]
Dollar.objects.bulk_create(obj)
