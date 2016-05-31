# Highcharts and Django

Highcharts and Django test examples.

```bash
git clone https://github.com/rg3915/highcharts.git
cd highcharts
source setup.sh
```

## Tutorial

Veja o modelo

```python
# models.py
from django.db import models


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
```

Importando os dados de um CSV.

Variação do dólar

http://www.dolarhoje.net.br/dolar-comercial.php


```python
# dollar.csv
date,value
1/1/2016,3.956
4/1/2016,4.033
5/1/2016,3.994
6/1/2016,4.017
7/1/2016,4.052
8/1/2016,4.038
11/1/2016,4.049
...
```

```python
# shell_dollar.py
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
    d = i['date']
    # Transforma '%d/%m/%Y' para '%Y-%m-%d'.
    d = datetime.datetime.strptime(d, '%d/%m/%Y').strftime('%Y-%m-%d')
    obj = Dollar.objects.create(
        date=d,
        value=i['value']
    )


# done
```

```bash
touch graphics.py
```

```python
# graphics.py
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from .models import Dollar


def dollar_json(request):
    data = Dollar.objects.values('date', 'value')
    lista = [{'dia': i['date'], 'valor': float(i['value'])} for i in data]
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)
```

```python
# core/urls.py
from django.conf.urls import url
from highcharts.core.graphics import dollar_json
from highcharts.core.views import dollar_graphic

urlpatterns = [
    url(r'^dollar-graphic/$', dollar_graphic),
    url(r'^dollar_json/$', dollar_json),
]
```

```python
# urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'', include('highcharts.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
]
```

View para o Template.

```python
# views.py
from django.shortcuts import render


def dollar_graphic(request):
    return render(request, 'dollar_graphic.html')
```

Dentro da pasta `highcharts/core/` crie a pasta `templates`.

```bash
mkdir templates
touch templates/base.html
touch templates/dollar_graphic.html
```

```html
# base.html
<html>
<head>
  <meta charset="UTF-8">
  <title>Highcharts</title>

  <!-- jQuery -->
  <script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
  <!-- HighCharts JS -->
  <script src="http://code.highcharts.com/highcharts.js"></script>

</head>
<body>
  <div class="container">
    {% block content %}{% endblock content %}
    {% block js %}{% endblock js %}
  </div>
</body>
</html>
```

```html
# dollar_graphic.html
{% extends "base.html" %}
{% load static %}

{% block content %}
  <div id="dollar-chart"></div>
{% endblock %}

{% block js %}
  <script src="{% static 'js/dollar_graphic.js' %}"></script>
{% endblock js %}
```

```bash
mkdir -p static/js
touch static/js/dollar_graphic.js
```

```js
# dollar_graphic.js
$(function () {
    var url = "/dollar_json/";

    $.getJSON(url, function(res){
        console.log(res);
        /* Transformando o dicionário em lista.
           Com o comando map eu coloco uma lista dentro da outra,
           necessário para este tipo de gráfico. */
        var data = res.map(function (v) {
            return [v.dia, v.valor]
        });

        console.log(data);

        $('#dollar-chart').highcharts({
            chart: {
                type: 'line'
            },
            title: {
                text: 'Variação do Dólar'
            },
            xAxis: {
                type: 'category'
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Valor'
                },
                plotOptions: {
                    line: {
                        dataLabels: {
                            enabled: true
                        },
                    }
                },
            },
            legend: {
                enabled: false
            },
            series: [{
                data: data,
                dataLabels: {
                    enabled: true,
                    align: 'center',
                    style: {
                        fontSize: '15px'
                    }
                }
            }],
        });
    });
});
```

Porcentagem de produtos por categoria


# Projeto antigo

Veja o [projeto antigo](old.md).