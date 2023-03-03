from django.urls import re_path

from proxy.dev_server.api import dev_server_proxy_handler

app_name = "dev_server"

urlpatterns = [
    re_path(r"^dev/v1/", dev_server_proxy_handler, name="dev_server_proxy_handler"),
]
