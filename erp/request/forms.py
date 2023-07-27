from django import forms
from django.urls import reverse
from django.shortcuts import redirect
from .models import RequestOrder, RequestItem
from distributor.models import Item, Distributor, Brand

# Import from other apps

class OrderForm(forms.ModelForm):
    class Meta:
        model = RequestOrder
        fields = [
            'id',
            'distributor',
            'discount',
        ]
        exclude = ('created', 'id')
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = RequestItem
        fields = [
            'item',
            'qty',
            'cost',
        ]
    # def __init__(self, brand_get, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['item'].queryset = Item.objects.filter(brand_id=brand_get)

        