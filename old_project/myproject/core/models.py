from django.db import models


class Continent(models.Model):
    continent = models.CharField(max_length=30)

    class Meta:
        ordering = ['continent', ]

    def __str__(self):
        return self.continent


class Population(models.Model):
    continent = models.ForeignKey('Continent')
    year = models.PositiveIntegerField()
    population = models.PositiveIntegerField()

    class Meta:
        ordering = ['year', 'continent']

    def __str__(self):
        return "{} {} {}".format(self.continent, self.year, self.population)
