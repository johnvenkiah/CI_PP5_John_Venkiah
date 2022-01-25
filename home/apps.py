"""
home/apps.py: config file for home app
"""

# - - - - - Django Imports - - - - - - - - -
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Home app Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
