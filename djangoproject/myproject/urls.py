from django.conf.urls import url
from django.contrib import admin
import myproject.core.views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^population/json$', v.population_list_json, name='population_list_json'),
    url(r'^admin/', admin.site.urls),
]
