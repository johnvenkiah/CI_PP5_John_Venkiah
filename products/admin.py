"""
products/admin.py: Admin models for superuser capabilities with models
Category, Product and Review. Based on admin in
Code Institute's Boutique Ado project.
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
        'brand',
        'price',
        'gender',
        'size_type',
        'rating',
        'discount',
        'image_url',
        'image',
    )
    list_filter = (
        'category',
        'brand',
        'gender',
        'is_new'
    )
    search_fields = [
        'art_nr',
        'name',
    ]

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
        'image_url',
        'image',
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
    search_fields = [
        'user__username',
        'title',
        'product__name'
    ]
    list_per_page = 15


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Review, ReviewAdmin)
