from django.db import models
from django.utils import timezone

# Import models from other apps
from distributor.models import Item
from request.models import RequestItem

# Create your models here.

class Batch(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    lot = models.CharField(max_length=20)
    expiry = models.DateField(default="4637-11-25")
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.lot

class InventoryIn(models.Model):
    lot = models.ForeignKey(Batch, on_delete=models.CASCADE)
    request = models.ForeignKey(RequestItem, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

class InventoryOut(models.Model):
    lot = models.ForeignKey(Batch, on_delete=models.CASCADE)
    qty = models.IntegerField()
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)