"""
products/forms.py: forms to be used with the product app of the application
"""

# - - - - - Django Imports - - - - - - - - -
from django.forms import Textarea, Select, ModelForm, CharField, ImageField

# - - - - - Internal Imports - - - - - - - - -
from .widgets import ProductClearableFileInput, BrandClearableFileInput
from .models import Product, Category, Review, Brand

# - - - - - 3rd Party Imports - - - - - - - - -
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


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
        model = Product
        exclude = ('rating', 'discount',)

    image = ImageField(
        label='Image',
        required=False,
        widget=ProductClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.helper = FormHelper()
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['image'].widget.attrs['id'] = 'new-product-image'

        self.fields['price'].widget.attrs['placeholder'] = '€0.00'
        self.fields['initial_price'].widget.attrs['placeholder'] = '€0.00'

        # self.helper.layout = Layout(
        #     Row(
        #         Column('field1', css_class='form-group col-md-2 mb-0'),
        #         Column('field2', css_class='form-group col-md-2 mb-0'),
        #         css_class='form-row'
        #     ),
        # )

    description = CharField(
        widget=Textarea(
            {
                'rows': 5,
                'class': 'textarea',
            }
        )
    )


class BrandForm(ModelForm):
    """
    Form for admins to create an instance of the brand model,
    aka add a new brand to the site.
    """

    class Meta:
        model = Brand
        fields = '__all__'

    image = ImageField(
        label='Image',
        required=False,
        widget=BrandClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        brands = Brand.objects.all()
        friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['name'].choices = friendly_names
        self.fields['image'].widget.attrs['id'] = 'new-brand-image'