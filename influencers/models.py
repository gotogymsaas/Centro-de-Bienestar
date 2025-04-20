from django.db import models
from django.conf import settings
from products.models import Product
from orders.models import Order

class Influencer(models.Model):
    user       = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code       = models.SlugField(unique=True)
    commission = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)

    def __str__(self):
        return f"{self.user.username} ({self.code})"

class ReferralClick(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    source_ip  = models.GenericIPAddressField(null=True, blank=True)

class OrderReferral(models.Model):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    order      = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount     = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.order.id} → {self.influencer.code}"
