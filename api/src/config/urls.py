from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from v1.views import ProductViewSet, SponsorViewSet

router = routers.SimpleRouter()

router.register(r"api/v1/products", ProductViewSet)
router.register(r"api/v1/sponsors", SponsorViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls

admin.site.site_header = "Event Menu API Admin"
admin.site.site_title = "Event Menu API Admin Portal"
admin.site.index_title = "Welcome to Event Menu API Portal"
