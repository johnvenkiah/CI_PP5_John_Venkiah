from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='my_stepup'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
]
