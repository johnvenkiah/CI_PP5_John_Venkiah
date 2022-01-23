"""
cart/test_views.py: testing of views in cart app.
functionality for it. Largely guided by pmeeny's Love Rugby project:
https://github.com/pmeeny/CI-MS4-LoveRugby
"""
# - - - - - Django Imports - - - - - - - - -
from django.contrib.messages import get_messages
from django.test import TestCase

# Internal:
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCartViews(TestCase):
    """
    Testing of cart views
    """
    def setUp(self):
        """
        Create a test product
        """
        # pylint: disable=no-member
        Product.objects.create(
            art_nr='999',
            name='Test Name',
            price='99.99',
            description='This is a description of the product',
        )

    def tearDown(self):
        """
        Delete test products
        """
        Product.objects.all().delete()  # pylint: disable=no-member

    def test_show_cart_page(self):
        """
        Tests that the cart page is displayed
        """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_empty_cart(self):
        """
        Tests adding a product to an empty cart
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        response = self.client.post(f'/cart/add/{product.id}/', {
                'quantity': 1,
                'redirect_url': 'view_cart'
            }
        )
        cart = self.client.session['cart']
        self.assertEqual(cart[str(product.id)], 1)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Added Test Name to your cart')

    def test_update_item_quantity_to_two(self):
        """
        Tests updating cart item quantity to 2
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        response = self.client.post(f'/cart/update/{product.id}/', {
            'quantity': 2
        })
        cart = self.client.session['cart']
        self.assertEqual(cart[str(product.id)], 2)
        messages = list(get_messages(response.wsgi_request))
        product_id = cart[str(product.id)]
        self.assertEqual(str(messages[0]), 'Updated Test Name quantity to '
                         + str(product_id))

    def test_update_cart_quantity_to_zero(self):
        """
        Tests updating the cart item quantity from 1 to 0
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        response = self.client.post(f'/cart/add/{product.id}/', {
            'quantity': 1, 'redirect_url': 'view_cart',
        })
        self.assertRedirects(response, '/cart/')
        cart = self.client.session['cart']
        self.assertEqual(cart[str(product.id)], 1)
        response = self.client.post(f'/cart/update/{product.id}/', {
            'quantity': 0, 'redirect_url': 'view_cart',
        })
        self.assertRedirects(response, '/cart/')
        cart = self.client.session['cart']
        self.assertEqual(cart, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Removed Test Name from your cart')

    def test_remove_product_from_cart(self):
        """
        Tests removing a product from the cart
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        self.client.post(f'/cart/add/{product.id}/', {
            'quantity': 1, 'redirect_url': 'view_cart',
        })
        cart = self.client.session['cart']
        self.assertEqual(cart[str(product.id)], 1)
        response = self.client.post(f'/cart/remove/{product.id}/')
        cart = self.client.session['cart']
        self.assertEqual(cart, {})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[1]), 'Removed Test Name from your cart')

    def test_remove_product_from_cart_exception(self):
        """
        This test tries to remove a product from a cart
        that doesnt exist, and an exception is thrown is verified
        """
        # pylint: disable=no-member
        product = Product.objects.get(art_nr='999')
        response = self.client.post(f'/cart/remove/{product.id}/')
        self.assertEqual(
            500, response.status_code
        )
