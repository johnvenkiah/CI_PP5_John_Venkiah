"""
home/views.py: Views for home app, rendering the landing page of the site.
"""

# - - - - - Django Imports - - - - - - - - -
from django.views.generic import TemplateView
from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy

# - - - - - 3rd Party imports - - - - - - - - -

# - - - - - Internal imports - - - - - - - - -


class HomeView(TemplateView):
    """
    Class to display the landing page of the site, index.html.
    """
    template_name = 'home/index.html'


class CustomPasswordChangeView(PasswordChangeView):
    """
    Class to override the success URL directly to the home page after
    changing the password. Inherits from the Django PasswordChangeView.
    https://github.com/pennersr/django-allauth/blob/master
    /allauth/account/views.py

    Tips from here:
    https://stackoverflow.com/questions/
    60150124/django-allauth-passwordchangeview
    -override-of-success-url-with-logged-out-user
    """
    
    success_url = reverse_lazy('home')  # <- choose your URL
