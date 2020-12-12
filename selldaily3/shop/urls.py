from django.urls import path,include
from . import views
import users.views as viewss


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', viewss.register_view, name='register'),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path('api/', include('shop.api.urls')),
    path('check/',views.checkout),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()), # new
    path('cancelled/', views.CancelledView.as_view()), # new
]
