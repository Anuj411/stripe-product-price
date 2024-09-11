from django.shortcuts import render
from django.views.generic import CreateView

from app_modules.organization.forms import OrganizationForm
from app_modules.organization.models import Organization

class OrganizationRegisterView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "organization/register.html"