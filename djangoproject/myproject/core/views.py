import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from itertools import chain
from .models import Continent, Population


def home(request):
    continents = Continent.objects.all()

    pop1800 = Population.objects.values('population').filter(year='1800')
    pop1900 = Population.objects.values('population').filter(year='1900')
    pop2008 = Population.objects.values('population').filter(year='2008')

    context = {'continents': continents, 'Year1800': pop1800,
               'Year1900': pop1900, 'Year2008': pop2008}
    return render(request, 'index.html', context)


def population_list_json(request):
    continents = Continent.objects.all()

    pop1800 = Population.objects.all().filter(year='1800')
    pop1900 = Population.objects.all().filter(year='1900')
    pop2008 = Population.objects.all().filter(year='2008')

    context = list(chain(continents, pop1800, pop1900, pop2008))
    s = serializers.serialize("json", context)
    return HttpResponse(s)
