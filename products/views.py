from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Brand, Review
from .forms import ReviewForm
from .products_choices import GENDER_CHOICES

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
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
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
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
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)

        if review_form.is_valid():

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
