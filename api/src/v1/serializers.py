from rest_framework import serializers

from v1.models import Product, Sponsor


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "image", "display"]


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ["name", "url_social_media", "image"]
