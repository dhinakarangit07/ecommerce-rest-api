from rest_framework import viewsets
from django.contrib.auth.models import User

from .models import Cart
from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):

    serializer_class = CartSerializer

    def get_queryset(self):

        user = User.objects.first()

        return Cart.objects.filter(user=user)

    def perform_create(self, serializer):

        user = User.objects.first()

        serializer.save(user=user)