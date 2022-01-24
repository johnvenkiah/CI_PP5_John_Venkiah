"""
user_account/test_views.py: testing of user_account app views
"""

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

# pylint: disable=no-member


class TestUserAccountViews(TestCase):
    """
    Testing of user_account views
    """
    def setUp(self):
        """
         This setup creates a test user
         """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        testuser.save()

    def tearDown(self):
        """
        Delete test user
        """
        User.objects.all().delete()

    def test_load_delete_account_page(self):
        """
        Test to check if the delete page is loaded
        """
        user = User.objects.all()[0]
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(f'/user_account/delete/{user.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_account/delete_account.html')

    def test_account_deletion(self):
        """
        Checks to 
        """
        user = User.objects.get()
        self.client.login(username='test_user', password='test_password')
        response = self.client.post(f'/user_account/delete/{user.id}')
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Account deleted successfully.')
