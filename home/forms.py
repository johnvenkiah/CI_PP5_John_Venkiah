"""
home/forms.py: contains the contact form accessible through contexts.py
in the home directory.
"""
# - - - - - Django Imports - - - - - - - - -
from django import forms


class ContactForm(forms.Form):
    """
    The contact form from which users send emails to the site owner.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Full Name',
            'from_email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        for field in self.fields:
            self.fields[field].required = True
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['aria-label'] = placeholder
            self.fields[field].label = False

    name = forms.CharField(
        max_length=100
    )
    from_email = forms.EmailField(
        max_length=100
    )
    subject = forms.CharField(
        max_length=100
    )
    message = forms.CharField(
        max_length=254,
        widget=forms.Textarea(
            {
                'rows': 5,
                'class': 'textarea',
            }
        )
    )

    def __str__(self):
        return f'Email form: {self.email}'
