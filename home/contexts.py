"""
home/contexts.py: contains functions to be accessed in templates
throughout the site: contact form and mobile.
"""
# - - - - - Native Python imports - - - - - - - - -
import re

# - - - - - Internal imports - - - - - - - - -
from home.forms import ContactForm
# pylint: disable=unused-argument, invalid-name


def contact_form(request):
    """
    Function returns the contact form throughout the site.

    Args: request (the request object)
    """
    return {'contact_form': ContactForm}


def mobile(request):
    """
    Function returns True if the request comes from a mobile device.
    Credits: https://stackoverflow.com/questions/42273319/'
        'detect-mobile-devices-with-django-and-python-3

    Args: request (the request object)
    """

    mobile_agent_re = re.compile(
        r".*(iphone|mobile|androidtouch)", re.IGNORECASE
    )
    try:

        if mobile_agent_re.match(request.META['HTTP_USER_AGENT']):
            is_mobile = True

        else:
            is_mobile = False
            # pylint: disable=broad-except
    except Exception:
        is_mobile = False

    return {'is_mobile': is_mobile}
