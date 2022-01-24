"""
products/test_views.py: testing of product app views
Credit: https://github.com/pmeeny/CI-MS4-LoveRugby
"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase

# - - - - - Internal imports - - - - - - - - -
from .models import Category, Product, Review, Brand
# pylint: disable=no-member


class TestProductViews(TestCase):
    """
    A class for testing product views
    """
    def setUp(self):
        """
        Create test user(regular and super user), category and product
         """
        User.objects.create_user(
            username='test_user',
            password='test_password',
        )

        User.objects.create_superuser(
            username='test_super_user',
            password='test_password',
        )

        Category.objects.create(
            name='test-category', friendly_name='Test Category')

        Brand.objects.create(
            name='test-brand', friendly_name='Test Brand')

        Product.objects.create(
            name='Test Name',
            gender='u',
            price=100,
            art_nr='999',
            size_type='shoes',
            description='Test Description',
            details='Test Details',
        )

    def tearDown(self):
        """
        Delete test user, category, product
        """
        User.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        Brand.objects.all().delete()

    def test_get_all_products(self):
        """
        This test tests get all products page and verifies
        """
        response = self.client.get(
            '/products/', {
                'search_term': 'test',
                'current_categories': 'sneakers',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_search_all_products_no_query_string(self):
        """
        This test tests search all products with no query string
        """
        response = self.client.get('/products/', {'q': ''})
        self.assertRedirects(response, '/products/')

    def test_search_all_products_category_string(self):
        """
        This test tests search all product category string
        """
        response = self.client.get('/products/', {'category': 'sneakers'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_sort(self):
        """
        This test tests product sort with parameters
        """
        response = self.client.get('/products/', {'sort': 'name'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get('/products/', {'sort': 'category'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        response = self.client.get(
            '/products/', {
                'sort': 'category',
                'direction': 'desc'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """
        This test tests get product details page and verifies
        """
        product = Product.objects.get()
        response = self.client.get(
            f'/products/{product.id}/', {
                'product': product,
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product_page_as_superuser(self):
        """
        This test tests add product page as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(response, 'products/add_product_brand.html')

    def test_add_product_page_as_non_superuser(self):
        """
        This test tests add product page as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Sorry, access to that page is denied.')

    def test_add_product_as_superuser_post(self):
        """
        This test tests add product page as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        response = self.client.post('/products/add/', {
            'name': 'Test Name 2',
            'art_nr': '1000',
            'price': 100,
            'size_type': 'shoes',
            'description': 'Test Description',
            'details': 'Test Details',
        })
        self.assertRedirects(response, '/products/2/')

    def test_get_edit_product_page(self):
        """
        This test tests edit product page(get) as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.get(f'/products/edit/{product.id}/')
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_edit_product_page_as_superuser(self):
        """
        This test tests edit product page(post) as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        self.client.post(f'/products/edit/{product.id}/', {
            'name': 'Test Updated Name',
            'art_nr': '999',
            'price': 110,
            'size_type': 'shoes',
            'description': 'Test Updated description',
            'details': 'Test Updated details',
        })
        updated_product = Product.objects.get()
        self.assertEqual(updated_product.name, 'Test Updated Name')
        self.assertEqual(
            updated_product.description, 'Test Updated description'
        )
        self.assertEqual(updated_product.details, 'Test Updated details')

    def test_edit_product_page_as_non_superuser(self):
        """
        This test tests edit product page as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/edit/{product.id}/', {
            'name': 'Test Updated Name',
            'price': 110,
            'art_nr': '999',
            'description': 'Test Updated description',
            'details': 'Test Updated details',
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), 'Sorry, access to that page is denied.'
        )

    def test_delete_product_as_superuser(self):
        """
        This test tests delete product as a superuser and verifies
        """
        self.client.login(username='test_super_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Product "{product.name}" successfully deleted'
        )
        deleted_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(deleted_product), 0)

    def test_delete_product_as_non_superuser(self):
        """
        This test tests delete product as a non superuser and verifies
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.get()
        response = self.client.post(f'/products/delete/{product.id}/')
        self.assertRedirects(response, '/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), 'Sorry, access to that page is denied.'
        )

    def test_add_review_to_product(self):
        """
        This test tests add review to product as a success case and verifies
        """
        test_user_1 = User.objects.create_user(
            username='test_user_1', password='test_password')
        self.client.login(username='test_user_1', password='test_password')
        product = Product.objects.get()

        Review.objects.create(
            user=test_user_1,
            title='Test Title',
            product=product,
            product_rating=5,
            user_review='Test Review',
        )
        response = self.client.post(
            f'/products/{product.id}/', {
                'title': 'Test Title',
                'product_rating': 5,
                'user_review': 'Test Review'
            }
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), (
                f'Thank you for reviewing "{product.name[:25]}.."! '
                f'You can now view and remove it below.'
                )
            )

    def test_delete_review_from_product(self):
        """
        This test tests delete review from a product and verifies
        """
        test_user_2 = User.objects.create_user(
            username='test_user_2', password='test_password')
        self.client.login(username='test_user_2', password='test_password')
        product = Product.objects.get()

        review = Review.objects.create(
            user=test_user_2,
            title='Test Review Title',
            product=product,
            product_rating=5,
            user_review='Test Review',
        )
        response = self.client.post(
            f'/products/delete_review/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), (
                f'Your review "{review.title}" of '
                f'{review.product} is now deleted'
            )
        )

    def test_review_changing_product_rating(self):
        """
        This test tests delete review from a product and verifies
        """
        product = Product.objects.get()
        test_user_3 = User.objects.create_user(
            username='test_user_3',
            password='test_password',
            email='test_3@email.com',
        )
        self.client.login(username='test_user_3', password='test_password')
        Review.objects.create(
            user=test_user_3,
            title='Test Title 1',
            product=product,
            product_rating=5,
            user_review='Test Review User 3',
        )
        test_user_4 = User.objects.create_user(
            username='test_user_4',
            password='test_password',
            email='test_4@email.com',
        )
        self.client.login(username='test_user_4', password='test_password')
        Review.objects.create(
            user=test_user_4,
            title='Test Title 2',
            product=product,
            product_rating=4,
            user_review='Test Review User 3',
        )
        self.assertEqual(product.rating, 4.5)
