"""
user_account.forms.py - includes user deletion form.
"""

from django.utils.safestring import mark_safe
from django import forms


class DeleteUserForm(forms.Form):
    """
    Simple form that provides a checkbox that signals deletion or user account.
    form copied from https://github.com/pennersr/django-allauth/pull/2785
    """
    delete_checkbox = forms.BooleanField(
        label=mark_safe(
            'Tick this box and click Delete Account below to confirm'
        ), required=True
    )

    def __init__(self, *args, **kwargs):
        super(DeleteUserForm, self).__init__(*args, **kwargs)
