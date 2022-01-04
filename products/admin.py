"""
products/admin.py: Admin models for superuser capabilities with models
Category, Product and Review
"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin

# - - - - - Internal imports - - - - - - - - 
from .models import Product, Category, Brand, Review
#  - - - - - - - - - - - - - - - - - - - - -


class ProductAdmin(admin.ModelAdmin):
    """
    The Admin product class
    """
    list_display = (
        'art_nr',
        'name',
        'category',
        'price',
        'description',
        'gender',
        'brand',
        'details',
        'size_type',
        'rating',
        'discount',
        'image_url',
        'image',
    )
    list_filter = (
        'art_nr',
        'category',
        'brand',
        'gender',
        'name',
        'price',
    )
    search_fields = (
        'art_nr',
        'category',
        'brand',
        'name',
        'price',
    )

    ordering = ('art_nr',)


class CategoryAdmin(admin.ModelAdmin):
    """
    The Admin category class
    """
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    """
    The Brand category class
    """
    list_display = (
        'friendly_name',
        'name',
        'logo_url',
        'logo',
    )


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin class for the Review model.
    """
    list_display = (
        'user',
        'product',
        'product_rating',
        'title',
        'user_review',
        'date_created',
    )
    list_filter = (
        'user',
        'product',
        'product_rating',
        'date_created',
    )
    search_fields = (
        'user',
        'product',
        'product_rating'
        'title',
    )
    list_per_page = 15


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Review, ReviewAdmin)
