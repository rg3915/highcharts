import csv
import datetime as dt
from highcharts.core.models import Euro

euro_list = []

''' Lendo os dados de euro.csv '''
with open('highcharts/fix/euro.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        # Convert '%d/%m/%Y' to '%Y-%m-%d'.
        d = dt.datetime.strptime(dct['date'], '%d/%m/%Y').strftime('%Y-%m-%d')
        euro_list.append((d, dct['value']))
    f.close()


obj = [Euro(date=val[0], value=val[1]) for val in euro_list]
Euro.objects.bulk_create(obj)
