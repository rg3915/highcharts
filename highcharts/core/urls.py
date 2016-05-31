from django.conf.urls import url
from highcharts.core.graphics import dollar_json
from highcharts.core.views import dollar_graphic

urlpatterns = [
    url(r'^dollar-graphic/$', dollar_graphic),
    url(r'^dollar_json/$', dollar_json),
]
