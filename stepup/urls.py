"""stepup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# - - - - - Internal Imports - - - - - - - - -
from home.views import CustomPasswordChangeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'accounts/password/change/',
        CustomPasswordChangeView.as_view(),
        name="account_change_password",
    ),
    path('accounts/', include('allauth.urls')),
    path('user_account/', include('user_account.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('my_stepup/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
