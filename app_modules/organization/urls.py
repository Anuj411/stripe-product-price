from django.urls import path
from app_modules.organization import views

urlpatterns = [
    path('register/', views.OrganizationRegisterView.as_view(), name="register_organization"),
]
