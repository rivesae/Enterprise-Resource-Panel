import uuid
from django.db import models
from core.models import CustomUser
from django.utils import timezone

# Import models from other apps
from distributor.models import Item
from request.models import RequestItem

# Create your models here.

class Batch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    lot = models.CharField(max_length=20)
    expiry = models.DateField(default="4637-11-25")
    active = models.BooleanField(default=True)
    created = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='batch_dateandtime_created')
    date_deleted = models.DateTimeField(null=True, blank=True)
    deleted = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='batch_dateandtime_deleted')

    def __str__(self):
        return self.lot

class InventoryIn(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lot = models.ForeignKey(Batch, on_delete=models.CASCADE)
    request = models.ForeignKey(RequestItem, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    created = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='invin_dateandtime_created')
    date_deleted = models.DateTimeField(null=True, blank=True)
    deleted = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='invin_dateandtime_deleted')

class InventoryOut(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lot = models.ForeignKey(Batch, on_delete=models.CASCADE)
    qty = models.IntegerField()
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    created = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='invout_dateandtime_created')
    date_deleted = models.DateTimeField(null=True, blank=True)
    deleted = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='invout_dateandtime_deleted')