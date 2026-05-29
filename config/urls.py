
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cart/', cart_page),
    path('login/', login_page),
    path('checkout/', checkout_page),
    path('product/<int:id>/', product_detail),
    # User Registration
    path('api/users/', include('users.urls')),

    path('api/', include('products.urls')),

    path('api/', include('cart.urls')),

    path('api/orders/', include('orders.urls')),

]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )