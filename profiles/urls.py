"""
profiles/urls.py: urls for profile app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='my_stepup'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
    path(
        'add_to_wishlist/<int:product_id>',
        views.add_to_wishlist,
        name='add_to_wishlist'
    ),
    path(
        'remove_from_wishlist/<int:product_id>',
        views.remove_from_wishlist,
        name='remove_from_wishlist'
    ),
]
