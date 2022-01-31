"""
profiles/views.py: views for profile app.
Credit to Code Institute for profile and order_history views.
"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# - - - - - Internal Imports - - - - - - - - -
from products.models import Product
from checkout.models import Order
from .models import UserProfile, WishListItem
from .forms import UserProfileForm

# pylint: disable=no-member


@login_required
def profile(request):
    """
    Allows users to view and edit their info and Wishlist,
    as well as viewing their order history.
    Args:
        request (the request object)
    Returns:
        the MyStepUp profile page
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    try:
        wishlist = WishListItem.objects.filter(user=request.user.id)[0]
    except IndexError:
        wishlist_items = None
    else:
        wishlist_items = wishlist.product.all()

    if not wishlist_items:
        messages.info(request, 'Your Wishlist is empty!')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles/my_stepup.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist_items': wishlist_items,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Adds the product to the users Wishlist.
    Args:
        request (the request object)
        product_id (the product in question)
    Returns:
        the MyStepUp profile page
    """
    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlistitem = get_object_or_404(WishListItem, user=request.user.id)

    except Http404:
        wishlistitem = WishListItem.objects.create(user=request.user)
    if product in wishlistitem.product.all():
        messages.info(request, 'Your Wishlist contains this product already,')
    else:
        wishlistitem.product.add(product)
        messages.info(
            request, f'Added {product.name[:30]}.. to your Wishlist.'
        )
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Removes a product from the users Wishlist.
    Args:
        request (the request object)
        product_id (the product in question)
    Returns:
        A redirect to the previously viewed page
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlistitem = get_object_or_404(WishListItem, user=request.user.id)
    if product in wishlistitem.product.all():
        wishlistitem.product.remove(product)
        messages.info(
            request, f'Removed {product.name[:30]} from your Wishlist'
        )
    else:
        messages.error(
            request, (
                f'{product.name[:30]}.. is not in your Wishlist.'
            )
        )

    # Return the previously viewed page
    return redirect(request.META.get('HTTP_REFERER'))


def order_history(request, order_number):
    """
    Returns the users order history.
    Args:
        request (the request object)
        order_number (the order instance)
    Returns:
        the order confirmation page (template and context)
    """
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
