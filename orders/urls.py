from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .api_views import *

urlpatterns = [
    url(r'^v1/orders/$', OrderList.as_view(), name='orders_list'),
    url(r'^v1/orders/customer/(?P<customer_id>-?\d+)/$', orders_by_customer, name='orders_by_customer'),

]

urlpatterns = format_suffix_patterns(urlpatterns)