from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("mtom.api.urls", "api"))),
    path("proxy/", include("proxy.dev_server.urls", namespace="dev_server")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
