"""
checkout/urls.py: urls for the checkout app
"""

# - - - - - Django Imports - - - - - - - - -
from django.urls import path

# - - - - - Internal Imports - - - - - - - - -
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order_confirmation/<order_number>',
         views.order_confirmation,
         name='order_confirmation'),
    path('cache_checkout_data/',
         views.cache_checkout_data,
         name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
