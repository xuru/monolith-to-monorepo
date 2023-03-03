# Register your models here.
from django.contrib import admin

from proxy.dev_server.models import UserProxyRegister


@admin.register(UserProxyRegister)
class UserProxyRegisterAdmin(admin.ModelAdmin):
    list_display = ("user", "market_always_open")
