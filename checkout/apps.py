"""
checkout/apps.py: config file for checkout app
"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout app Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        # pylint: disable=unused-import, import-outside-toplevel
        import checkout.signals  # noqa
