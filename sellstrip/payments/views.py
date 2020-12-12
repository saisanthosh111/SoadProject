import stripe
import requests
import json
from django.shortcuts import render
from django.conf import settings # new
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView

def checkout(request):
    if request.method == "POST":
        url = "http://127.0.0.1:8000/shop/api/orders/"
        headers = {
                  'Authorization': "Token bd7e1cbff069629cb7a982e3c8151185a5a4afa9",
            }
        querystring = {"items_json":request.POST.get('itemsJson', ''),
        "name" : request.POST.get('name', ''),
        "amount" : request.POST.get('amount', ''),
        "email" : request.POST.get('email', ''),
        "address" : request.POST.get('address', ''),
        "city" : request.POST.get('city', ''),
        "state" : request.POST.get('state', ''),
        "zip_code" : request.POST.get('zip_code', '')}
        # r = json.dumps(querystring)
        response = requests.post(url,headers=headers,data=querystring)
        # res=response.json()
        print(querystring)
    return render(request,"checkout.html")


def home_view(request):
    url = "http://127.0.0.1:8000/shop/api/products/watches"
    headers = {
          'Authorization': "Token f36930a1a93a7313e258da33c539956182355b2c",
    }
    response = requests.request("GET", url, headers=headers)
    # res = response.json()
    res=response.json()
    context = {"res":res}
    # print(res)
    return render(request,"home.html",context)

def stripe_config(request):
        if request.method == 'GET':
            stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
            return JsonResponse(stripe_config, safe=False)

def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:7000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'usb',
                        'quantity': 1,
                        'currency': 'inr',
                        'amount': '200',

                    }


                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
class SuccessView(TemplateView):
     template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'
