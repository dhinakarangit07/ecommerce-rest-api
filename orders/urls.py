from django.urls import path
from .views import (
    PlaceOrderAPIView,
    OrderHistoryAPIView,
    OrderDetailAPIView,
)

urlpatterns = [

    # Place Order
    path('place/', PlaceOrderAPIView.as_view(), name='place-order'),

    # Order History
    path('history/', OrderHistoryAPIView.as_view(), name='order-history'),

    # Order Details
    path('<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
]

from django.urls import path
from .views import CreatePaymentAPIView

urlpatterns = [
    path('create-payment/', CreatePaymentAPIView.as_view()),
]

from django.urls import path

from .views import (
    CreatePaymentAPIView,
    VerifyPaymentAPIView
)

urlpatterns = [

    path(
        'create-payment/',
        CreatePaymentAPIView.as_view()
    ),

    path(
        'verify-payment/',
        VerifyPaymentAPIView.as_view()
    ),

]