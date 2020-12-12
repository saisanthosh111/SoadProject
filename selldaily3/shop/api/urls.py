from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('products/<str:pk>',views.Product_list_name_get, name="product_list_name_get"),
    path('products/',views.Product_list_view_get, name="product_list_view"),
    path('orders/',views.Order_list_view_post, name="order_list_view_post"),
    path('orders/<slug:slug>',views.Order_detail_view_get, name="order_detail_view"),
    path('register/',views.registration_view,name='register'),
    path('login/',obtain_auth_token,name="login")
    # path('api/', include('survey.api.urls'))
]
