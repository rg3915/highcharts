import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from .models import Dollar, Euro


def dollar_json(request):
    data = Dollar.objects.values('date', 'value')
    lista = [{'dia': i['date'], 'valor': float(i['value'])} for i in data]
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)


def euro_json(request):
    data = Euro.objects.values('date', 'value')
    lista = [{'dia': i['date'], 'valor': float(i['value'])} for i in data]
    resp = json.dumps(lista, cls=DjangoJSONEncoder)
    return HttpResponse(resp)
