"""
review_form.py: form for 
"""

# - - - - - Django Imports - - - - - - - - -
from django.forms import Textarea, Select, ModelForm, CharField

# - - - - - Internal imports - - - - - - - - -
# from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ReviewForm(ModelForm):
    """
    Form for users to create reviews and ratings for products.
    """
    class Meta:
        """
        Meta class defining the available fields and their attributes.
        """
        model = Review
        fields = (
            'title',
            'product_rating',
            'user_review',
        )

        widgets = {
            'product_rating': Select(
                attrs={
                    'id': 'product_rating',
                    'class': 'custom-select'
                }
            ),
            'user_review': Textarea(
                attrs={
                    'rows': 5
                }
            ),
        }
