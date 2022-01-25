"""
checkout/webhooks.py: Contains webhook listener for stripe payment
Credit: Code Institute, Boutique Ado project, Stripe
"""

# - - - - - Django Imports - - - - - - - - -
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# - - - - - 3rd party Imports - - - - - - - - -
import stripe

# - - - - - Internal Imports - - - - - - - - -
from checkout.webhook_handler import StripeWH_Handler
# pylint: disable=invalid-name, broad-except


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listens for webhooks from Stripe
    """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler as h to conform with line length rules
    h = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': h.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': h.handle_payment_intent_payment_failed
    }

    # Get the webhook type from Stripe
    event_type = event['type']

    # If there's a handler for it, get it from the event map
    # Use the generic one by default
    event_handler = event_map.get(event_type, h.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response
