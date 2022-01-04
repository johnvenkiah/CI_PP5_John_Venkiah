"""
products/models.py: Contains the models Category, Product and Review
"""

# - - - - - Django Imports - - - - - - - - -
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# - - - - - 3rd Party imports - - - - - - - - -

# - - - - - Internal imports - - - - - - - - -
from .products_choices import GENDER_CHOICES, SIZE_CHOICES, RATING_CHOICES


class Category(models.Model):
    """
    The Category model class, with fields for the category name
    """
    class Meta:
        """
        Category Meta class for returning plural name
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns category name as a string
        Args:
            object: self
        Returns:
            Category name field as string
        """
        return f'{self.name}'

    def get_friendly_name(self):
        """
        Returns the category friendly name string
        Args:
            self (object): self.
        Returns:
            The category friendly name string
        """
        return self.friendly_name


class Product(models.Model):
    """
    The Product model class, used to generate an instance of a product
    """
    class Meta:
        """
        Meta class enables ordering of the product instances by id
        """
        ordering = ['id']

    art_nr = models.CharField(
        verbose_name=_('Art. Nr'),
        max_length=254
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=254
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    price = models.DecimalField(
        verbose_name=_('Price'),
        max_digits=6,
        decimal_places=2
    )
    description = models.TextField(
        verbose_name=_('Description'),
    )
    gender = models.CharField(
        verbose_name=_('Gender'),
        choices=GENDER_CHOICES,
        max_length=1
    )
    brand = models.CharField(
        verbose_name=_('Brand'),
        max_length=254,
    )
    details = models.CharField(
        verbose_name=_('Product Details'),
        max_length=254,
        null=True,
        blank=True
    )
    size_type = models.BooleanField(
        verbose_name=_('Size Type'),
        choices=SIZE_CHOICES,
        default='N/A',
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        verbose_name=_('Rating'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    discount = models.DecimalField(
        verbose_name=_('Discount'),
        default=0,
        max_digits=6,
        decimal_places=2,
    )
    image_url = models.URLField(
        verbose_name=_('Image URL'),
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        verbose_name=_('Image'),
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns Product name field
        Args:
            object: self
        Returns:
            Product name as a string
        """
        return f'{self.name}'


class Review(models.Model):
    """
    The Review model class, crating an instance of a review
    """
    class Meta:
        """
        Meta class enables ordering by id
        """
        ordering = ['id']

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    product_rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5
    )
    title = models.TextField(
        verbose_name=_('Review Title'),
        max_length=25,
        null=False,
        blank=False
    )
    user_review = models.TextField(
        verbose_name=_('User Review'),
        max_length=250,
        null=False,
        blank=False
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        Returns review title field as a string
        Args:
            self (object): self.
        Returns:
            The review text string
        """
        return f'{self.title}'