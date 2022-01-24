"""
profiles/test_models.py: Tests for models in profile app.
Credit: https://github.com/pmeeny/CI-MS4-LoveRugby
"""

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase
from django.contrib.auth.models import User

# - - - - - Internal imports - - - - - - - - -
from .models import UserProfile

# pylint: disable=no-member


class TestProfileModels(TestCase):
    """
    A class for testing the profile model
    """
    def setUp(self):
        """
        This setup creates a test user
        """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test_user@test.com')
        test_user.save()

    def tearDown(self):
        """
        Delete test user
        """
        User.objects.all().delete()

    def test_profile_str_method(self):
        """
        This test tests the users profile username
        """
        test_user = User.objects.get(username='test_user')
        profile = UserProfile.objects.get(user=test_user)
        self.assertEqual(str(profile), profile.user.username)
