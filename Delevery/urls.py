from django.urls import path

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views


app_name = 'Delivery'


urlpatterns = [

    path('delivery', views.post_delivery, name='posy_delivery'),
    path('success', views.order_received, name='success'),

]
