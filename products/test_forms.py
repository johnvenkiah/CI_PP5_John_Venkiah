"""
products/test_forms.py: Contains testing of the forms in the products app.
Credit: https://github.com/pmeeny/CI-MS4-LoveRugby
"""

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase

# - - - - - Internal Imports - - - - - - - - -
from .forms import ReviewForm, BrandForm, ProductForm


class TestReviewForm(TestCase):
    """
    Test that the checkout form is returned valid.
    """
    def test_review_form(self):
        """
        Here it is, the actual test.
        """
        form = ReviewForm({
            'title': 'Test review title',
            'product_rating': 3,
            'user_review': 'Test review',
            })
        self.assertTrue(form.is_valid())


class TestBrandForm(TestCase):
    """
    Test that the checkout form is returned valid.
    """
    def test_brand_form(self):
        """
        Here it is, the actual test.
        """
        form = BrandForm({
            'name': 'test_name',
            'friendly_name': 'Test Name',
            })
        self.assertTrue(form.is_valid())


class TestProductForm(TestCase):
    """
    Test that the checkout form is returned valid.
    """
    def test_product_form(self):
        """
        Here it is, the actual test.
        """
        form = ProductForm({
            'name': 'Test Name',
            'gender': 'u',
            'price': 100,
            'description': 'Test description',
            'details': 'Test detail',
            'size_type': 'shoes',
            })
        self.assertTrue(form.is_valid())
