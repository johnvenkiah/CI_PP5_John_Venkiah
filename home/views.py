"""
home/views.py: Views for home app, rendering the landing page of the site.
"""

# - - - - - Django Imports - - - - - - - - -
from django.views.generic import TemplateView
from django.views.generic import FormView
from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail

# - - - - - 3rd Party imports - - - - - - - - -

# - - - - - Internal imports - - - - - - - - -
from .forms import ContactForm
from stepup.settings import EMAIL_HOST_USER


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

    success_url = reverse_lazy('home')


class ContactView(FormView):
    """
    View for contact page
    """
    template_name = 'contact.html'
    model = User
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        msg1 = f"Mail from {form.cleaned_data['from_email']}\n\n"
        msg2 = '\n\nForm sent from StepUp via Django'
        cleaned_msg = f'{msg1}{form.cleaned_data["message"]}{msg2}'

        send_mail(
            form.cleaned_data['subject'],
            cleaned_msg,
            form.cleaned_data['from_email'],
            [EMAIL_HOST_USER],
            fail_silently=False
        )

        messages.success(
            self.request, 'Thanks for contacting us, we will reply shortly.'
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, (
                "Sorry, there was an error sending the message."
                "Try again later."
            )
        )
