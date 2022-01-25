"""
profiles/test_views.py: testing of profile app views
"""

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

# - - - - - Internal imports - - - - - - - - -
from checkout.models import Order
from profiles.models import UserProfile

# pylint: disable=no-member


class TestProfileViews(TestCase):
    """
    Testing of profile views
    """
    def setUp(self):
        """
         This setup creates a test user,
         test product and test order
         """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        testuser.save()

        Order.objects.create(
            order_number='12345678',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='test_user@test.com',
            phone_number='12345678',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def tearDown(self):
        """
        Delete test user and order
        """
        User.objects.all().delete()
        Order.objects.all().delete()

    def test_get_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (get) and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/my_stepup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/my_stepup.html')

    def test_post_profile_page(self):
        """
        This test logins a test user and
        accesses their profile page (post) and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.post('/my_stepup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/my_stepup.html')

    def test_get_order_detail_page(self):
        """
        This test logins a test user and accesses
        the order history page for a test order and verifies
        """
        self.client.login(username='test_user1', password='test_password')
        test_user = User.objects.get(username='test_user')
        order = Order.objects.get(email=test_user.email)
        response = self.client.get('/my_stepup/order_history/' +
                                   order.order_number)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'This is a past confirmation for '
                         'order number 12345678. ' +
                         'A confirmation email was sent on the order date.')
