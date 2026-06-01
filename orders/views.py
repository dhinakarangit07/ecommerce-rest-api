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

    user = User.objects.first()

    cart_items = Cart.objects.filter(user=user)

    if request.method == 'GET':

        total_price = sum(
            item.product.price * item.quantity
            for item in cart_items
        )

        return Response({
            "cart_count": cart_items.count(),
            "total_price": total_price
        })

    # POST
    if not cart_items.exists():
        return Response({
            "message": "Cart is Empty"
        }, status=400)

    total_price = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    order = Order.objects.create(
        user=user,
        total_price=total_price
    )

    cart_items.delete()

    return Response({
        "message": "Order Placed Successfully",
        "order_id": order.id,
        "total_price": total_price
    })