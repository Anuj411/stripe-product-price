from random import choices
from django.db import models

class Organization(models.Model):
    name = models.CharField("Organization Name", max_length=200)
    email = models.EmailField(unique=True)
    image = models.ImageField("Image", upload_to="organization/image/", null=True, blank=True)
    contact_person_name = models.CharField("Contact Person Name", max_length=200)
    contact_person_mobile = models.CharField("Contact Person Model", max_length=15)

    def __str__(self):
        return self.name


class Product(models.Model):
    stripe_product_id = models.CharField("Payment ID", max_length=300)
    name = models.CharField("Payment Name", max_length=200)
    image = models.ImageField("Image", upload_to="organization/product/image/", null=True, blank=True)
    stripe_price_id = models.CharField("Price ID", max_length=300, null=True, blank=True)
    unit_price = models.DecimalField("Price", max_digits=20, decimal_places=2, null=True, blank=True)
    reccuring = models.BooleanField("Reccuring", default=True, null=True, blank=True)

    def __str__(self):
        return self.name
    


class subscription(models.Model):
    FAILED = "failed"
    COMPLETED = "completed"

    STATUSES = (
        (FAILED, "Failed"),
        (COMPLETED, "Completed"),
    )

    product = models.ForeignKey(Product, related_name="subscription_set", on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organization, related_name="subscription_set", on_delete=models.CASCADE)
    product_price = models.DecimalField("Price", max_digits=20, decimal_places=2)
    start_date = models.DateTimeField("Start date", auto_now_add=True, null=True, blank=True)
    end_date = models.DateTimeField("End date", null=True, blank=True)
    is_activate = models.BooleanField("Is Activate", default=True)
    payment_amount = models.DecimalField("Amount", decimal_places=2, max_digits=10)
    payment_status = models.CharField("Payment Status", choices=STATUSES, max_length=100)
    payment_method = models.CharField("Payment Method", default="card", max_length=100)
    reason = models.TextField("Reason", null=True, blank=True)
    invoice = models.FileField("Invoice", upload_to="organization/subscription-invoice/", null=True, blank=True)

    def __str__(self):
        return self.organization.name
