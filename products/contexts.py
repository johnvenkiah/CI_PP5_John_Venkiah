"""
products/contexts.py: Contains code so brand is accessible through the navbar
throughout the whole site.
"""

# - - - - - Internal imports - - - - - - - - -
from .models import Brand


def get_brands(request):
    all_brands = Brand.objects.all()
    return {
        'all_brands': all_brands,
    }

