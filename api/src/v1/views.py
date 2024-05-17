from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from v1.models import Product, Sponsor
from v1.serializers import ProductSerializer, SponsorSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
