from django.urls import path
from app_modules.register import views

urlpatterns = [
    path('organization/', views.OrganizationRegisterView.as_view(), name="register_organization"),

]
