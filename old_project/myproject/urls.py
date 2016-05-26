from django.conf.urls import url
from django.contrib import admin
import myproject.core.views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^barchart/$', v.barchart, name='barchart'),
    url(r'^columnchart/$', v.columnchart, name='columnchart'),

    url(r'^population/json/$', v.population_list_json, name='population_list_json'),
    url(r'^admin/', admin.site.urls),
]
