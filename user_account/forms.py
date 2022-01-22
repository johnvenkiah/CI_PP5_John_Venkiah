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
            'Are you sure you want to delete your account?'
        ), required=True
    )

    def __init__(self, *args, **kwargs):
        super(DeleteUser, self).__init__(*args, **kwargs)
