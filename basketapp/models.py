from django.conf import settings
from django.db import models

from mainapp.models import Games


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Games, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    add_datetime = models.DateTimeField(auto_now_add=True)
