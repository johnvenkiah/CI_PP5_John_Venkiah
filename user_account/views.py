from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from .forms import DeleteUserForm


class DeleteAccountView(DeleteView):
    """
    Removes a user instance using Django's generic DeleteView
    """

    model = User
    form = DeleteUserForm
    success_url = reverse_lazy('home')
    template_name = 'delete_account.html'
    success_message = 'Account deleted successfully.'

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
