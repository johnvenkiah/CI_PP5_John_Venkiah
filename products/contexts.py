"""
products/contexts.py: Contains function so all brands are accessible via
the navbar throughout the whole site.
"""

# - - - - - Internal imports - - - - - - - - -
from .models import Brand

# pylint: disable=unused-argument, no-member


def get_brands(request):
    """
    Gets all instances of the brand model.
    Args:
        request (object)
    Returns:
        All brand instances registered on the site.
    """
    all_brands = Brand.objects.all()
    return {
        'all_brands': all_brands,
    }
