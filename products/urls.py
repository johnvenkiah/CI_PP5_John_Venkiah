"""
products/urls.py: All urls for the products app.
"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.urls import path

# - - - - - Internal Party imports - - - - - - - - -
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('manage_brands/', views.manage_brands, name='manage_brands'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product_brand, name='add_product_brand'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/', views.delete_product, name='delete_product'
    ),
    path(
        'update_brand/<int:brand_id>/', views.update_brand, name='update_brand'
    ),
    path(
        'delete_brand/<int:brand_id>/', views.delete_brand, name='delete_brand'
    ),
]
