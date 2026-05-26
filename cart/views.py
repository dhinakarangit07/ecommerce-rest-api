from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Cart
from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):

    serializer_class = CartSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)