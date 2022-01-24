"""
products/test_models.py: Tests for models in products app
"""
# - - - - - Django Imports - - - - - - - - -
from django.contrib.auth.models import User
from django.test import TestCase

# - - - - - Internal imports - - - - - - - - -
from products.models import Category, Product, Review, Brand
# pylint: disable=no-member


class TestProductModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test user, category, product and review
        """
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@email.com'
        )

        Category.objects.create(
            name='test-category',
            friendly_name='Test Category'
        )

        test_brand = Brand.objects.create(
            name='test-brand',
            friendly_name='Test Brand'
        )

        product = Product.objects.create(
            name='Test Name',
            price=100,
            brand=test_brand,
            art_nr='999',
            description='Test Description',
            details='Test Details',
        )
        Review.objects.create(
            user=test_user,
            title='Test Title',
            product=product,
            product_rating=5,
            user_review='Test review text',
        )

    def tearDown(self):
        """
        Delete test user, category, product and review
        """
        User.objects.all().delete()
        Category.objects.all().delete()
        Brand.objects.all().delete()
        Product.objects.all().delete()
        Review.objects.all().delete()

    def test_category_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_brand_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        brand = Brand.objects.get(name='test-brand')
        self.assertEqual((brand.__str__()), brand.name)
        self.assertEqual(brand.get_friendly_name(), brand.friendly_name)

    def test_product_str_method(self):
        """
        This test tests the products str method and verifies
        """
        product = Product.objects.get(art_nr='999')
        self.assertEqual((product.__str__()), product.name)

    def test_review_str_method(self):
        """
        This test tests the reviews str method and verifies
        """
        review = Review.objects.get(title='Test Title')
        self.assertEqual((review.__str__()), review.title)
