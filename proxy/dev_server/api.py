from django.views.decorators.csrf import csrf_exempt

from proxy.dev_server.views import proxy_view


@csrf_exempt
def dev_server_proxy_handler(request, data=None):
    url = request.get_full_path().replace("/proxy/dev", "/someother/dev")
    request_args = None
    if data:
        request_args = {"data": data}
    return proxy_view(request, url, request_args)
