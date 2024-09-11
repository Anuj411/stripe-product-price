
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organization/', include('app_modules.organization.urls')),
    path('stripe/webhook/', views.stripe_webhook, name='stripe-webhook'),
]
