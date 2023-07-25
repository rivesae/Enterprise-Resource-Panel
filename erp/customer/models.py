from django.db import models
from django.utils import timezone

from distributor.models import Item

# Create your models here.

now = timezone.localtime()

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    tin = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    # series
    # employee
    active = models.IntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now)

class Sell(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255)
    active = models.IntegerField(null=True)
    date_created = models.DateTimeField(default=timezone.now)