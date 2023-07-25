from django.shortcuts import render
from .models import Batch
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Importing models from other apps
from distributor.models import Brand, Item

def index(request):
    return render(request, 'inventory/index.html')