"""
user_account/views.py: views for the user_account app
"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from .forms import DeleteUserForm


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    """
    Removes a user instance using Django's generic DeleteView
    """

    model = User
    form = DeleteUserForm()
    success_url = '/'
    template_name = 'user_account/delete_account.html'
    success_message = 'Account deleted successfully.'

    def get_context_data(self, **kwargs):
        form = DeleteUserForm()
        context = super().get_context_data(**kwargs)
        context["form"] = form

        return context

    def delete(self, request, *args, **kwargs):
        """
        Removes a user instance on the site
        Args:
            self (self object)
            request (request object)
            *args
            **kwargs
        Returns:
            the delete product page with the form and context.
        """

        messages.success(self.request, self.success_message)
        return super(DeleteAccountView, self).delete(request, *args, **kwargs)
