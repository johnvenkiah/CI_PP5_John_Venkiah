"""
products/views.py: views to display all pages in the products app.
"""

# - - - - - Django Imports - - - - - - - - -
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

# - - - - - Internal imports - - - - - - - - -
from .models import Product, Category, Brand, Review
from .forms import ReviewForm, ProductForm, BrandForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()  # pylint: disable=no-member
    query = None
    categories = None
    gender = None
    gender_pretty = ""
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
                gender_pretty = "Men's"
            if 'w' in gender:
                gender_pretty = "Women's"

        if 'news' in request.GET:
            products = products.filter(is_new=True)

        if 'on_sale' in request.GET:
            products = products.filter(~Q(initial_price=price))

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'gender': gender,
        'gender_pretty': gender_pretty,
        'brands': brands,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show details for a specific product.
    """

    product = get_object_or_404(Product, pk=product_id)
    # pylint: disable=no-member
    reviews = Review.objects.filter(product=product)
    print(type(product.price), type(product.initial_price))

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():

            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()

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
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Adds a product to the site
    Args:
        request (object)
    Returns:
        the delete product page with the form and context.
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, access to that page is denied.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(
            request.POST, request.FILES, prefix='product'
        )

        if product_form.is_valid():

            product = product_form.save()
            product.art_nr = f'SU202200{str(product.id)}'

            if product.discount and product.discount > 0:
                product.discount = product.initial_price - product.price
                product.initial_price = None
            product_form.validate_initial_price()
            product.save()

            messages.success(request, f'Successfully added {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Add Product failed. \
                    please check if the form is valid and try again.')
    else:
        product_form = ProductForm(prefix='product')

    if request.method == 'POST' and not product_form.is_valid():
        brand_form = BrandForm(request.POST, prefix='brand')
        product_form = ProductForm(prefix='product')
        if brand_form.is_valid():
            brand = brand_form.save()
            messages.success(
                request, f'Successfully added {brand.friendly_name}'
            )
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Add Brand failed. \
                    please check if the form is valid and try again.')

    else:
        brand_form = BrandForm(prefix='brand')

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
        'brand_form': brand_form,
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

            product_form.save()

            if product.discount and product.discount > 0:
                product.discount = product.initial_price - product.price
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
    messages.success(request, f'Product "{product.name}" deleted!')
    return redirect(reverse('products'))
