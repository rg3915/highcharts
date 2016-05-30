import csv
import datetime
from highcharts.core.models import Euro

euro_list = []

''' Lendo os dados de euro.csv '''
with open('highcharts/fix/euro.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        euro_list.append(dct)
    f.close()


for i in euro_list:
    d = i['date_euro']
    # Transforma '%d/%m/%Y' para '%Y-%m-%d'.
    d = datetime.datetime.strptime(d, '%d/%m/%Y').strftime('%Y-%m-%d')
    obj = Euro.objects.create(
        date_euro=d,
        value=i['value']
    )


# done
