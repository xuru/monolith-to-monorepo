from django.db import models


class UserProxyRegister(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    market_always_open = models.BooleanField(default=False, help_text="Allow user to trade stocks 24/7")
