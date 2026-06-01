from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from django.contrib.auth.models import User

from cart.models import Cart
from .models import Order


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def place_order(request):

    cart_items = Cart.objects.all()

    if request.method == 'GET':

        total_price = sum(
            item.product.price * item.quantity
            for item in cart_items
        )

        return Response({
            "cart_count": cart_items.count(),
            "total_price": total_price
        })

    if not cart_items.exists():
        return Response({
            "message": "Cart is Empty"
        }, status=400)

    user = cart_items.first().user