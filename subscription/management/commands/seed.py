from django.conf import settings
# from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management import call_command
import stripe

from app_modules.organization.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

class Command(BaseCommand):
    help = "Seed Migrations."

    def __init__(self):
        # self.user_class = get_user_model()
        super().__init__()

    def handle(self, *args, **options):
        apps = settings.LOCAL_APPS
        for app in apps:
            call_command("makemigrations", app.split(".")[-1])
        call_command("migrate")
        self.create_stripe_product_and_prices()

    def create_stripe_product_and_prices(self):
        products = stripe.Product.list(active=True)
        for product in products.data:
            # print(f"==>> product: {product}")
            new_product, created = Product.objects.get_or_create(stripe_product_id = product.id)
            if product.default_price:
                new_product.stripe_price_id = product.default_price
                price = stripe.Price.retrieve(product.default_price)

                new_product.unit_price = price.unit_amount / 100
                new_product.reccuring = True if price.recurring == "true" else False
            new_product.name = product.name
            new_product.image = product.images[0] if product.images else ""
            new_product.save()

        self.stdout.write("Products are synced.")
