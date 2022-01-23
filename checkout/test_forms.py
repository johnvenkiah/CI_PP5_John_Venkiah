"""
checkout/test_forms.py: Contains testing of the Orderform in checkout app.
"""

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase

# Internal:
from .forms import OrderForm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutForm(TestCase):
    """
    Test that the checkout form is returned valid.
    """
    def test_order_form(self):
        """
        Here it is, the actual test.
        """
        form = OrderForm({
            'full_name': 'Test Name',
            'email': 'test@email.com',
            'phone_number': '1234567890',
            'country': 'SE',
            'town_or_city': 'Stockholmsburg',
            'street_address1': 'Rabb Street 2',
            'street_address2': 'Stockholms County',
            })
        self.assertTrue(form.is_valid())
