from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, WishListAdd
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        wishlist = WishListAdd.objects.filter(user=request.user)
    except IndexError:
        messages.error(
            'Sorry, we were not able to retrieve your wishlist at the moment'
        )
        wishlist = None
    else:
        wishlist_items = wishlist.products.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/my_stepup.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist': wishlist,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/order_confirmation.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
