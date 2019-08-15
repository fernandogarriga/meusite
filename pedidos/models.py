from django.conf import settings
from django.db import models
from django.utils import timezone


class Pedido(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produtos = models.TextField(max_length=200)
    endereco = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.autor
