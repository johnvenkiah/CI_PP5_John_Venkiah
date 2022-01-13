"""
home/views.py: Views for home app, rendering the landing page of the site.
"""

# - - - - - Django Imports - - - - - - - - -
from django.views.generic import TemplateView

# - - - - - 3rd Party imports - - - - - - - - -

# - - - - - Internal imports - - - - - - - - -


class HomeView(TemplateView):
    """
    Class to display the landing page of the site, index.html.
    """
    template_name = 'home/index.html'
