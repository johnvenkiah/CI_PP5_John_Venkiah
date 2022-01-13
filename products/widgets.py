"""
product/widget.py: Allows customisation of the image field in the product and
brand forms. This functionality is derived from the Boutique Ado project with
Code Institute.
"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class ProductClearableFileInput(ClearableFileInput):
    """
    Defines contents of the html elements of the imported widget from django.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/product_clearable_file_input.html'
    )


class BrandClearableFileInput(ClearableFileInput):
    """
    Defines contents of the html elements of the imported widget from django.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/brand_clearable_file_input.html'
    )
