"""
home/test_views: testing of views in home app
"""

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Tests returning the index.html page
    """
    def test_get_home_page(self):
        """
        This test checks that the index page
        is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
