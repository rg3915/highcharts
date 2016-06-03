import json
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from .models import Dollar, Euro, Product


def dollar_json(request):
    data = Dollar.objects.values('date', 'value')
    lista = [{'dia': i['date'], 'valor': float(i['value'])} for i in data]
    return JsonResponse({'dollar': lista})


def euro_json(request):
    data = Euro.objects.values('date', 'value')
    lista = [[i['date'], float(i['value'])] for i in data]
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)


def product_json(request):
    ''' Porcentagem de produtos por categoria '''
    data = Product.objects.values('category')\
        .annotate(value=Count('category'))\
        .order_by('category').values('category', 'category__category', 'value')
    total = Product.objects.all().count()
    ''' Podemos reescrever o dicionário com nossos próprios nomes de campos. '''
    lista = [{'categoria': item['category__category'],
              'porcentagem': float((item['value'] / total) * 100)} for item in data]
    s = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(s)
