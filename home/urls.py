"""
home/urls.py: All urls for the home app.
"""

# - - - - - Django Imports - - - - - - - - - -
from django.urls import path

# - - - - - 3rd Party imports - - - - - - - - -

# - - - - - Internal Party imports - - - - - - - - -
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
