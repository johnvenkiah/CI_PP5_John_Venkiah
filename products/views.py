"""
products/views.py: views to display all pages in the products app.
"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

# - - - - - Internal imports - - - - - - - - -
from profiles.models import WishListItem
from .models import Product, Category, Brand, Review
from .forms import ReviewForm, ProductForm, BrandForm

# pylint: disable=no-member


def all_products(request):
    """
    Enables displaying products on the products page,
    depending on the users sorting or queries.
    Args:
        request (object)
    Returns:
        The products page and its context.
    """

    products = Product.objects.all()
    wishlist = WishListItem.objects.filter(user=request.user.id)
    query = None
    categories = None
    gender = None
    gender_pretty = []
    brands = None
    sort = None
    direction = None
    price = None
    context = {}

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            # pylint: disable=no-member
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            # pylint: disable=no-member
            brands = Brand.objects.filter(name__in=brands)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            products = products.filter(gender__in=gender)

            if 'm' in gender:
                gender_pretty.append("Men's")
            if 'w' in gender:
                gender_pretty.append("Women's")

        if 'news' in request.GET:
            products = products.filter(is_new=True)

        if 'on_sale' in request.GET:
            products = products.filter(~Q(initial_price=price))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = Q(
                    name__icontains=query
            ) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'gender': gender,
        'gender_pretty': gender_pretty,
        'brands': brands,
        'wishlist': wishlist,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Displays a dedicated page for a specific product.
    Args:
        request (object)
    Returns:
        the product detail page and its context
    """

    product = get_object_or_404(Product, pk=product_id)
    try:
        wishlistitem = get_object_or_404(WishListItem, user=request.user.id)
    except Http404:
        wishlistitem = {}
        wishlist = None
    else:
        wishlist = wishlistitem.product.all()
    # pylint: disable=no-member
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():

            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(
                request, (
                    f'Thank you for reviewing "{product.name[:25]}.."! '
                    'You can now view and remove it below.'
                )
            )

            if product.rating:
                product.rating = (product.rating + review.product_rating) / 2
            else:
                product.rating = review.product_rating
            product.save()

            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'wishlist': wishlist,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product_brand(request):
    """
    Add a product or brand to the site
    Args:
        request (object)
    Returns:
        the add product or brand page with the form and context.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(
            request.POST, request.FILES, prefix='product'
        )
        brand_form = BrandForm(request.POST, prefix='brand')

        if product_form.is_valid():

            product = product_form.save()

            if product.initial_price and product.initial_price > 0:
                product.discount = product.initial_price - product.price
            else:
                product.initial_price = None
            product.art_nr = f'SU202200{product.id}'

            product_form.validate_initial_price()
            product.save()
            messages.success(
                request, f'Successfully added {product.name} to Products'
            )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Add Product failed. \
                    Please check if the form is valid and try again.')
    else:
        product_form = ProductForm(prefix='product')
        brand_form = BrandForm(prefix='brand')

    template = 'products/add_product_brand.html'
    context = {
        'product_form': product_form,
        'brand_form': brand_form,
    }

    return render(request, template, context)


@login_required
def add_brand(request):
    """
    Adds a brand to the site
    Args:
        request (object)
    Returns:
        the manage_brands page if the form is valid, otherwise returns
        the add_product_brand page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        brand_form = BrandForm(request.POST, request.FILES, prefix='brand')
        product_form = ProductForm(prefix='product')

        if brand_form.is_valid():
            brand = brand_form.save()
            messages.success(
                request, f'Successfully added {brand.friendly_name} to Brands'
            )
            return redirect(reverse('manage_brands'))
        else:
            messages.error(
                request, (
                    'Add Brand failed. '
                    'Please check if the form is valid and try again.'
                )
            )
            brand_form = BrandForm(prefix='brand')
            return redirect(reverse('add_product_brand'))

    else:
        brand_form = BrandForm()

    template = 'products/manage_brands.html'
    context = {
        'brand_form': brand_form,
        'product_form': product_form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product on the site
    Args:
        request (object)
        product_id (to get instance of the product to edit)
    Returns:
        the product edit page with the form and context.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(
            request.POST, request.FILES, instance=product
        )

        if product_form.is_valid():

            product = product_form.save()

            if product.initial_price and product.initial_price > 0:
                product.discount = product.initial_price - product.price
            else:
                product.initial_price = None

            product_form.validate_initial_price()
            product.save()

            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Updating Product failed. \
                    please check if the form is valid and try again.')
    else:
        product_form = ProductForm(instance=product)
        messages.info(request, f'Currently editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'product_form': product_form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Removes a product on the site
    Args:
        request (object)
        product_id (to get instance of the product to edit)
    Returns:
        the delete product page with the form and context.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product "{product.name}" successfully deleted')
    return redirect(reverse('products'))


@login_required
def manage_brands(request):
    """
    Site owner feature to manage brands on the site.
    Args:
        request (object)
    Returns:
        the manage_brands page with the form and context.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))

    sort = None
    direction = None
    brands = Brand.objects.all()  # pylint: disable=maybe-no-member
    form = BrandForm(request.POST)
    form_set = []
    for brand in brands:
        form = BrandForm(request.POST or None, instance=brand)
        form_set.append(form)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                brands = brands.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            brands = brands.order_by(sortkey)
    current_sorting = f'{sort}_{direction}'

    if request.method == 'POST':
        form = BrandForm(request.POST)

    template = 'products/manage_brands.html'
    context = {
        'brands': brands,
        'brand_context': (zip(brands, form_set)),
        'current_sorting': current_sorting,
    }
    return render(request, template, context)


@login_required
def update_brand(request, brand_id):
    """
    Removes a product on the site
    Args:
        request (object)
        product_id (to get instance of the product to delete)
    Returns:
        the manage_brands page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))
    brand = get_object_or_404(Brand, pk=brand_id)
    form = BrandForm(request.POST, request.FILES, instance=brand)
    if form.is_valid():
        brand = form.save()
        messages.success(
            request, f'Brand "{brand.friendly_name}" successfully updated'
        )
    else:
        form = BrandForm(request.POST, request.FILES, instance=brand)
        messages.error(
            request, (
                'Brand failed to be updated. Check that the name is unique, '
                'that the filetype is valid and try again.'
            )
        )
    return redirect(reverse('manage_brands'))


@login_required
def delete_brand(request, brand_id):
    """
    Removes a brand on the site
    Args:
        request (object)
        brand_id (to get instance of the brand to delete)
    Returns:
        the manage_brands page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))
    brand = get_object_or_404(Brand, pk=brand_id)

    try:
        brand.delete()
        messages.success(
            request, f'Brand "{brand.friendly_name}" successfully deleted'
        )

    except Exception as e:  # pylint: disable=broad-except, invalid-name
        messages.error(request, f'Error removing brand: {e}')
        return HttpResponse(status=500)

    return redirect(reverse('manage_brands'))


def delete_review(request, review_id):
    """
    Removes a product on the site
    Args:
        request (object)
        product_id (to get instance of the product to edit)
    Returns:
        the delete product page with the form and context.
    """

    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    try:
        review.delete()
        messages.success(
            request, (
                f'Your review "{review.title}" of {review.product} '
                'is now deleted'
            )
        )

    except Exception as e:  # pylint: disable=broad-except, invalid-name
        messages.error(request, f'Error removing review: {e}')
        return HttpResponse(status=500)

    return redirect(reverse('product_detail', args=[product.id]))
