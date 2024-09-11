import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app_modules.organization.models import Product

from django.conf import settings
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = 'whsec_1616197f9d8187f0c765adf8538bd843abecaa5a4c5194036112789912ded6de'

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return JsonResponse({'status': 'invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError:
        return JsonResponse({'status': 'invalid signature'}, status=400)

    # Handle the event
    print(f"==>> event['type']: {event['type']}")

    if event['type'] == 'price.updated':
        # Extract data
        price_data = event['data']['object']

        stripe_price_id = price_data['id']
        new_price = price_data['unit_amount']
        print(f"==>> new_price: {new_price}")

        # Update the price in your models
        try:
            product = Product.objects.get(stripe_price_id=stripe_price_id)
            print(f"==>> product: {product}")
            product.unit_price = new_price / 100  # Stripe sends the price in cents
            product.save()
        except Product.DoesNotExist:
            # Handle the case where the product is not found
            pass

    return JsonResponse({'status': 'success'}, status=200)
