"""
user_account/urls.py: contains the user delete url.
"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.urls import path

# - - - - - Internal Party imports - - - - - - - - -
from . import views


urlpatterns = [
    path(
        'delete/<int:pk>',
        views.DeleteAccountView.as_view(),
        name='delete_account'
    ),
]
