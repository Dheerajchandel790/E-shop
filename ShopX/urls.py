from django.contrib import admin
from django.urls import path
from ShopApp.views import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from ShopApp.form import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name="home"),
    path('details/<int:id>/',ProductDetails.as_view(), name="details"),
    path('search/', search, name="search"),
    path('add-to-carts/', addToCart, name="addCart"),
    path('carts/', carts, name="carts"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('buynow/', buynow, name="buynow"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),  
    path('checkout/',checkout, name="checkout"),
    path('registration/',RegistrationView.as_view(), name="registration"),

    path("remove/<id>", RemoveCart_items, name="remove"),
    path('profile/', profile, name='profile'),

    path('base/', base, name="base"),
    path('search/', search, name="search"),
    path('shoes/<slug:x>/', shoes, name='shoes'),
    path('mens/<slug:x>/', mens, name="mens"),
    path('womens/<slug:x>/', womens, name="womens"),
    path('camera/<slug:x>/', camera, name="camera"),
    path('sunglasses/<slug:x>/', sunglasses, name="sunglasses"),

] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
