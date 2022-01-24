"""
home/test_forms.py: Contains testing of the ContactForm in checkout app.
"""

# - - - - - Django Imports - - - - - - - - -
from django.test import TestCase

# - - - - - Internal Imports - - - - - - - - -
from .forms import ContactForm


class TestHomeForm(TestCase):
    """
    Test that the checkout form is returned valid.
    """
    def test_contact_form(self):
        """
        Here it is, the actual test.
        """
        form = ContactForm({
            'name': 'Test Name',
            'from_email': 'test@email.com',
            'subject': 'Message',
            'message': 'Hello, this is a message',
            })
        self.assertTrue(form.is_valid())
