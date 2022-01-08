"""
products/models.py: Contains the models Category, Product and Review
"""

# - - - - - Django Imports - - - - - - - - -
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# - - - - - Internal imports - - - - - - - - -
from .products_choices import sizes
from .products_choices import GENDER_CHOICES, SIZE_CHOICES, RATING_CHOICES


class Category(models.Model):
    """
    The Category model class, with fields for the category name.
    """
    class Meta:
        """
        Category Meta class for returning plural name.
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
        Returns the category name as string.
        Args:
            self (object)
        Returns:
            The category name field as string
        """
        return f'{self.name}'

    def get_friendly_name(self):
        """
        Returns the user readable category name as string.
        Args:
            self (object)
        Returns:
            The category friendly name string
        """
        return self.friendly_name


class Brand(models.Model):
    """
    The Brand model class, containing name and logo fields
    """
    class Meta:
        """
        Brand Meta class for returning plural name
        """
        verbose_name_plural = 'Brands'

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    logo_url = models.URLField(
        verbose_name=_('Image URL'),
        max_length=1024,
        null=True,
        blank=True
    )
    logo = models.ImageField(
        verbose_name=_('Logo'),
        null=True,
        blank=True
    )

    def __str__(self):
        """
        Returns brand name as a string
        Args:
            self (object)
        Returns:
            Brand name field as string
        """
        return f'{self.name}'

    def get_friendly_name(self):
        """
        Returns the user readable brand name
        Args:
            self (object)
        Returns:
            The brand friendly name string
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
    initial_price = models.DecimalField(
        verbose_name=_('Initial Price'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
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
        max_length=24,
        default='u'
    )
    brand = models.ForeignKey(
        'Brand',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    details = models.CharField(
        verbose_name=_('Product Details'),
        max_length=254,
        null=True,
        blank=True
    )
    size_type = models.CharField(
        verbose_name=_('Size Type'),
        choices=SIZE_CHOICES,
        max_length=24,
        default='N/A'
    )
    rating = models.DecimalField(
        verbose_name=_('Rating'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    is_new = models.BooleanField(
        verbose_name=('Is New'),
        default=False,
    )
    discount = models.DecimalField(
        verbose_name=_('Discount'),
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
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
        Returns the product name
        Args:
            self (object)
        Returns:
            The product name field as string
        """
        return f'{self.name}'

    def details_as_list(self):
        """
        Returns the product details as seperate strings
        Args:
            self (object)
        Returns:
            The product details as seperate strings
        """

        return self.details.split(',')  # noqa

    def get_sizes(self):
        """
        Returns the size type depending on the product type and gender
        Args:
            self (object)
        Returns:
            The product size choices
        """

        if self.size_type == 'shoes':
            if self.gender == 'w':
                return sizes['w_shoes']
            elif self.gender == 'm':
                return sizes['m_shoes']
            else:
                return sizes['shoes']

        elif self.size_type == 'socks':
            if self.gender == 'w':
                return sizes['w_socks']
            elif self.gender == 'm':
                return sizes['m_socks']
            else:
                return sizes['socks']
        else:
            return SIZE_CHOICES[2]


class Review(models.Model):
    """
    The Review model class, creating an instance of a review
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
    title = models.CharField(
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
            self (object)
        Returns:
            The review title
        """
        return f'{self.title}'
