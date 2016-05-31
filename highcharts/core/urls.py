from django.conf.urls import url
from highcharts.core.graphics import dollar_json, euro_json
from highcharts.core.views import dollar_graphic, euro_graphic

urlpatterns = [
    url(r'^dollar-graphic/$', dollar_graphic, name='dollar-graphic'),
    url(r'^euro-graphic/$', euro_graphic, name='euro-graphic'),
    url(r'^dollar_json/$', dollar_json),
    url(r'^euro_json/$', euro_json),
]
