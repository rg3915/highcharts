from django.contrib import admin
from .models import Population, Continent


class PopulationAdmin(admin.ModelAdmin):
    list_display = ('continent', 'year', 'population')
    list_filter = ('continent', 'year')

admin.site.register(Population, PopulationAdmin)
admin.site.register(Continent)
