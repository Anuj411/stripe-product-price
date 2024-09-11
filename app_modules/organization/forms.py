from django import forms
from app_modules.organization.models import Organization


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
    
