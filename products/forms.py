"""
products/forms.py: forms to be used with the product app of the application
"""

# - - - - - Django Imports - - - - - - - - -
from django.forms import (
    Textarea, Select, ModelForm, CharField, ImageField
)
from django.core.exceptions import ValidationError

# - - - - - Internal Imports - - - - - - - - -
from .widgets import ProductClearableFileInput, BrandClearableFileInput
from .models import Product, Category, Review, Brand


class ReviewForm(ModelForm):
    """
    Form for users to create reviews and ratings for products.
    """
    class Meta:
        """
        Meta class defining the available fields and their attributes.
        """
        model = Review
        fields = (
            'title',
            'product_rating',
            'user_review',
        )

        widgets = {
            'product_rating': Select(
                attrs={
                    'id': 'product_rating',
                    'class': 'custom-select'
                }
            ),
            'user_review': Textarea(
                attrs={
                    'rows': 5
                }
            ),
        }


class ProductForm(ModelForm):
    """
    The product form, used to create and edit products by admin users.
    """

    class Meta:
        """
        The defines the Product model and which fields to exclude.
        """
        model = Product
        exclude = ('rating', 'discount', 'art_nr',)

    def __init__(self, *args, **kwargs):
        """
        The defines the Product model and which fields to exclude.
        Args:
            self (object)
            args (arguments)
            kwargs (keyword arguments)
        """
        super(ProductForm, self).__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'initial_price': 'Initial Price if on sale (€)',
            'price': 'Price (€)',
            'description': 'Description',
            'details': 'Product Details (Seperate each with a comma)',
            'image_url': 'Image URL',
        }
        empty_labels = {
            'category': 'Select a category:',
            'brand': 'Select a brand:',
            'gender': 'Select a gender:',
            'size_type': 'Select size type for the product:',
        }
        categories = Category.objects.all()  # pylint: disable=no-member
        brands = Brand.objects.all()  # pylint: disable=no-member
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        brand_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = friendly_names
        self.fields['brand'].choices = brand_friendly_names
        self.fields['image'].widget.attrs['id'] = 'new-product-image'

        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['aria-label'] = placeholder
                self.fields[field].label = False

            if field in empty_labels:
                if self.fields[field].required:
                    empty_label = f'{empty_labels[field]} *'
                else:
                    empty_label = empty_labels[field]
                self.fields[field].empty_label = empty_label
                self.fields[field].widget.attrs['aria-label'] = empty_label
                self.fields[field].label = False

    image = ImageField(
        label='Image',
        required=False,
        widget=ProductClearableFileInput
    )

    description = CharField(
        widget=Textarea(
            {
                'rows': 4,
                'class': 'textarea',
            }
        )
    )

    details = CharField(
        widget=Textarea(
            {
                'rows': 2,
                'class': 'textarea',
            }
        )
    )

    def validate_initial_price(self):
        """
        This function makes sure that the price is never higher
        than the initial one.

        Args:
            self (object)
        """
        price = self.cleaned_data['price']
        initial_price = self.cleaned_data['initial_price']
        if initial_price and initial_price <= price:
            raise ValidationError(
                "Add an initial price only if the product is on sale " +
                "and has a lower current price."
            )


class BrandForm(ModelForm):
    """
    Form for admins to create an instance of the brand model,
    aka add a new brand to the site.
    """

    class Meta:
        """
        Defines the Brand model and that all model fields are included.
        """
        model = Brand
        exclude = ('name',)

    image = ImageField(
        label='Image',
        required=False,
        widget=BrandClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        This calls the super method on the form and
        sets attributes for the image field.
        Args:
            self (object)
            args (arguments)
            kwargs (keyword arguments)
        """
        super(BrandForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs['id'] = 'new-brand-image'
        self.fields['image'].widget.attrs['class'] = 'brand-img-class'

        placeholders = {
            'friendly_name': 'User-friendly name:',
            'image_url': 'Image URL',
        }

        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['aria-label'] = placeholder
                self.fields[field].label = False
