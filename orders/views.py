from rest_framework import generics, permissions
from .models import Order
from .serializers import OrderSerializer


# PLACE ORDER API
class PlaceOrderAPIView(generics.CreateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ORDER HISTORY API
class OrderHistoryAPIView(generics.ListAPIView):

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


# ORDER DETAILS API
class OrderDetailAPIView(generics.RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]



import razorpay
import hmac
import hashlib

from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

client = razorpay.Client(auth=(
    settings.RAZORPAY_KEY_ID,
    settings.RAZORPAY_KEY_SECRET
))

class CreatePaymentAPIView(APIView):

    def post(self, request):

        amount = request.data.get("amount")

        payment_data = {
            "amount": int(amount) * 100,
            "currency": "INR",
            "payment_capture": 1
        }

        order = client.order.create(data=payment_data)

        return Response({
            "message": "Payment created",
            "data": order
        })
    
class VerifyPaymentAPIView(APIView):

    def post(self, request):

        razorpay_order_id = request.data.get('razorpay_order_id')
        razorpay_payment_id = request.data.get('razorpay_payment_id')
        razorpay_signature = request.data.get('razorpay_signature')

        generated_signature = hmac.new(
            bytes(settings.RAZORPAY_KEY_SECRET, 'utf-8'),
            bytes(f"{razorpay_order_id}|{razorpay_payment_id}", 'utf-8'),
            hashlib.sha256
        ).hexdigest()

        if generated_signature == razorpay_signature:

            return Response({
                "message": "Payment verified successfully"
            })

        return Response({
            "message": "Payment verification failed"
        })