from django.db import models
from django.utils import timezone


# Importation of models in 'request' app (there seems to be an error: ImportError: cannot import name 'Distributor' from partially initialized module 'distributor.models' (most likely due to a circular import) )
# from request.models import RequestOrder

# Basic models for Items - Distributor

class Distributor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    tin = models.CharField(max_length=13, null=True, default="0000000000000")
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    PACKAGE_CHOICES = [
        ("BOX" , "BOX"),
        ("PC" , "PC"),
        ("CART" , "CART"),
        ("BOT" , "BOT"),
        ("SET" , "SET"),
        ("TRAY" , "TRAY"),
        ("PACK" , "PACK"),
        ("CRATE" , "CRATE"),
    ]

    PRINCIPAL = [
        ("BD", "Becton Dickinson"),
        ("OCD", "Ortho Clinical Diagnostics"),
        ("ARK", "Arkray Co. Ltd"),
    ]

    CATEGORY = [
        ("BDDS", "BD Diagnostics Systems"),
        ("BDPAS", "BD Pre-Analytical Systems"),
        ("BDB", "BD Biosciences"),
        ("MF", "Vitros Mainframe"),
        ("IH", "Vitros Immuno-hematology"),
        ("IA", "Vitros Immunoassay"),
    ]

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=40)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    other_pack = models.CharField(max_length=5, choices=PACKAGE_CHOICES, null=True)
    default_pack = models.CharField(max_length=5, choices=PACKAGE_CHOICES, null=True)
    max_conv = models.IntegerField(null=True)
    min_conv = models.IntegerField(null=True, blank=True)
    machine = models.BooleanField(default=False)
    parts = models.BooleanField(default=False)
    asset = models.BooleanField(default=False)
    principal = models.CharField(max_length=4, choices=PRINCIPAL, null=True, blank=True)
    category = models.CharField(max_length=7, choices=CATEGORY, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.name
    
# Linked model with 'inventory' app

# Copying information from 'request' app
class Purchase(models.Model):
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, null=True)
    request = models.IntegerField(null=True) # Copying the RequestOrder.id
    total = models.DecimalField(max_digits=10, decimal_places=2) # Totalling the amount from entry/inventoryin
    discount = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

class Entry(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2) # Copying cost from item upon entry. Cost will be the actual cost that time
    qty = models.IntegerField()
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)