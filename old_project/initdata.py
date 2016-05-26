# import random
from myproject.core.models import Continent, Population

continent = Continent.objects.get(continent='America')
Population.objects.create(continent=continent, year=1800, population=31)
Population.objects.create(continent=continent, year=1900, population=156)
Population.objects.create(continent=continent, year=2008, population=914)
continent = Continent.objects.get(continent='Asia')
Population.objects.create(continent=continent, year=1800, population=635)
Population.objects.create(continent=continent, year=1900, population=947)
Population.objects.create(continent=continent, year=2008, population=4054)
continent = Continent.objects.get(continent='Europe')
Population.objects.create(continent=continent, year=1800, population=203)
Population.objects.create(continent=continent, year=1900, population=408)
Population.objects.create(continent=continent, year=2008, population=732)
continent = Continent.objects.get(continent='Oceania')
Population.objects.create(continent=continent, year=1800, population=2)
Population.objects.create(continent=continent, year=1900, population=6)
Population.objects.create(continent=continent, year=2008, population=34)

continent = Continent.objects.get(continent='Africa')
Population.objects.create(continent=continent, year=1900, population=133)
Population.objects.create(continent=continent, year=2008, population=973)

print('Population salvo com sucesso.')
