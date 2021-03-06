"""
home/urls.py: all urls for the home app.
"""

# - - - - - Django Imports - - - - - - - - - - - - -
from django.urls import path

# - - - - - Internal Party imports - - - - - - - - -
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
