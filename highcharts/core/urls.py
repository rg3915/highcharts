from django.conf.urls import url
from highcharts.core.graphics import dollar_json, euro_json, product_json
from highcharts.core import views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^dollar-graphic/$', v.dollar_graphic, name='dollar-graphic'),
    url(r'^euro-graphic/$', v.euro_graphic, name='euro-graphic'),
    url(r'^product-graphic/$', v.product_graphic, name='product-graphic'),
    url(r'^dollar_json/$', dollar_json),
    url(r'^euro_json/$', euro_json),
    url(r'^product_json/$', product_json),
]
