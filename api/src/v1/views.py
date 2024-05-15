from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from v1.models import Product, Sponsor
from v1.serializers import ProductSerializer, SponsorSerializer

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@method_decorator(cache_page(CACHE_TTL), name="dispatch")
class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
