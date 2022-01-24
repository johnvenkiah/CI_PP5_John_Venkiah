import re

from home.forms import ContactForm


def contact_form(request):
    return {'contact_form': ContactForm}


def mobile(request):
    """
    Function returns True if the request comes from a mobile device.
    Credits: https://stackoverflow.com/questions/42273319/'
        'detect-mobile-devices-with-django-and-python-3

    Args: request (the request object)
    """

    MOBILE_AGENT_RE = re.compile(
        r".*(iphone|mobile|androidtouch)", re.IGNORECASE
    )

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        is_mobile = True

    else:
        is_mobile = False

    return {'is_mobile': is_mobile}
