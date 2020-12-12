from django.urls import path, include
import shop.views as shopviews
from . import views as userviews

urlpatterns = [
    path("contact", shopviews.contact, name="ContactUs"),
    path("about/", shopviews.about, name="AboutUs"),
    path("signup/", userviews.signup, name="signup"),
    path("login/", userviews.Login, name="login"),
 ]
