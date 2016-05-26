from myproject.core.models import Continent, Population

continent = Continent.objects.all()

pop1800 = Population.objects.values_list('population').filter(year='1800')
p1800 = [item[0] for item in pop1800]
pop1900 = Population.objects.values_list('population').filter(year='1900')
p1900 = [item[0] for item in pop1900]
pop2008 = Population.objects.values_list('population').filter(year='2008')
p2008 = [item[0] for item in pop2008]
