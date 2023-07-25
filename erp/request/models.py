from django.db import models
from django.utils import timezone
from core.models import CustomUser

# Importation of models from 'distributor' app
from distributor.models import Distributor, Item

now = timezone.localtime()

# Create your models here.

# For Purchase Order creation, linked with 'distributor' app
class RequestOrder(models.Model):
    STATUS = [
        ("Created", "Created"),
        ("Pending", "Pending"),
        ("Documented", "Documented"),
        ("Deleted", "Deleted"),
    ]

    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=4, null=True, default="0")
    delivery_dated = models.DateField(default=timezone.now, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)
    created = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_order')
    approved = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_order')
    date_documented = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)
    deleted = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='deleted_order')
    update = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS, null=True, default="Created")
    sent_to = models.CharField(max_length=255, null=True,blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        # If the parent is set to inactive, set all children to inactive as well
        if not self.active:
            self.requestitem_set.update(active=False)
            self.requestitem_set.update(delete_date=timezone.now)
        super(RequestOrder, self).save(*args, **kwargs)

class RequestItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    convert = models.BooleanField(default=False)
    package = models.CharField(max_length=5, null=True)
    request_order = models.ForeignKey(RequestOrder, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)
    delete_date = models.DateTimeField(null=True)
    date_created = models.DateTimeField(default=timezone.now)