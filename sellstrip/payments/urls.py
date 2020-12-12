#payments/urls.py
import stripe
from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_view, name ='home'),
    path('check/',views.checkout),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()), # new
    path('cancelled/', views.CancelledView.as_view()), # new
]
