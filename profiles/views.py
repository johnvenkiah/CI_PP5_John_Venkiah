from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, WishListItem
from .forms import UserProfileForm

from checkout.models import Order


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
    profile = get_object_or_404(UserProfile, user=request.user)

    try:
        wishlist = WishListItem.objects.filter(user=request.user.id)[0]
        if not wishlist:
            wishlist_items = None
    except IndexError:
        messages.error(
            request,
            'Sorry, we were not able to retrieve your wishlist at the moment'
        )
        wishlist_items = None
    else:
        wishlist_items = wishlist.products.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request,
                'Update failed. Please ensure the form is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

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
    wishlist = WishListItem.objects.filter(user=request.user.id)

    if product in wishlist.product.all():
        messages.error(request, 'This item is already in your Wishlist')

    else:
        new_add = WishListItem.objects.create(user=request.user)
        new_add.products.add(product)
        messages.success(
            request, f'Added {product.name[:30]}.. to your favourites'
        )
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist = WishListItem.objects.filter(user=request.user.id)

    if product not in wishlist.product.all():
        messages.error(request, 'This item is not in your Wishlist')
    else:
        wishlist.product.remove(product)
        messages.success(
            request, f'Removed {product.name[:30]}.. from your Wishlist'
        )
        return render(request.path)


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
