import csv
import datetime
from highcharts.core.models import Dollar

dollar_list = []

''' Lendo os dados de dollar.csv '''
with open('highcharts/fix/dollar.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        dollar_list.append(dct)
    f.close()


for i in dollar_list:
    d = i['date_dollar']
    # Transforma '%d/%m/%Y' para '%Y-%m-%d'.
    d = datetime.datetime.strptime(d, '%d/%m/%Y').strftime('%Y-%m-%d')
    obj = Dollar.objects.create(
        date_dollar=d,
        value=i['value']
    )


# done
