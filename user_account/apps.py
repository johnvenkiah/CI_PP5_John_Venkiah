"""
user_account/apps.py: config file for user_account app
"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class UserAccountConfig(AppConfig):
    """
    user_account app Config model
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_account'
