from django.shortcuts import render
from django.views.generic import CreateView

from subscription.app_modules.organization.forms import OrganizationForm

class OrganizationRegisterView(CreateView):
    form = OrganizationForm
    template_name = "register/organization-register.html"