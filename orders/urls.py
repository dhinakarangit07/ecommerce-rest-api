from django.urls import path

from .views import (
    PlaceOrderAPIView,
    OrderHistoryAPIView,
    OrderDetailAPIView,
    CreatePaymentAPIView,
    VerifyPaymentAPIView
)

urlpatterns = [

    # Orders
    path(
        'place/',
        PlaceOrderAPIView.as_view(),
        name='place-order'
    ),

    path(
        'history/',
        OrderHistoryAPIView.as_view(),
        name='order-history'
    ),

    path(
        '<int:pk>/',
        OrderDetailAPIView.as_view(),
        name='order-detail'
    ),

    # Payments
    path(
        'create-payment/',
        CreatePaymentAPIView.as_view(),
        name='create-payment'
    ),

    path(
        'verify-payment/',
        VerifyPaymentAPIView.as_view(),
        name='verify-payment'
    ),
]