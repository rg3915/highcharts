import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from itertools import chain
from .models import Continent, Population


def home(request):
    return render(request, 'index.html')


def barchart(request):
    return render(request, 'core/barchart.html')


def columnchart(request):
    return render(request, 'core/columnchart.html')


def population_list_json(request):
    ''' JSON used to generate the graphic '''
    continents = Continent.objects.all()

    pop1800 = Population.objects.all().filter(year='1800')
    pop1900 = Population.objects.all().filter(year='1900')
    pop2008 = Population.objects.all().filter(year='2008')

    context = list(chain(continents, pop1800, pop1900, pop2008))
    s = serializers.serialize("json", context)
    return HttpResponse(s)
