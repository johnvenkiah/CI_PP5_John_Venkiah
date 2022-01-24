"""
checkout/test_forms.py: Contains testing of the Orderform in checkout app.
"""
# pylint: disable=maybe-no-member

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase

# - - - - - Internal Imports - - - - - - - - -
from products.models import Product
from stepup import settings
from .models import Order
from .models import OrderLineItem


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create instances of Product and Order models
        """
        Product.objects.create(
            art_nr='999',
            name='Test Name',
            price='99.99',
            description='Test Description',
        )

        Order.objects.create(
            full_name='Test Name',
            email='test@gmail.com',
            phone_number='123456789',
            country='SE',
            town_or_city='Stockholmsburg',
            street_address1='Rabb Street 2',
        )

    def tearDown(self):
        """
        Delete test instances of Product and Order
        """
        Product.objects.all().delete()
        Order.objects.all().delete()

    def test_order_str_method(self):
        """
        Test that the order string method returns the order number
        """
        order = Order.objects.get(email='test@gmail.com')
        self.assertEqual(str(order), order.order_number)
