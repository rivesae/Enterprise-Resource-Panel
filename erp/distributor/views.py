from django.shortcuts import render
from .models import Distributor, Brand, Item
from .forms import Search
from django.db.models import Prefetch, Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

from django.utils.timezone import now
from django.utils import timezone

from django.core.paginator import Paginator
from django.views import View



@login_required(login_url='home:process')
def distributors(request):

    form_search = Search(request.GET)
    query = request.GET.get('search', '')

    if form_search.is_valid():
        results = Distributor.objects.filter( Q (name__icontains=query) | Q (address__icontains=query)).filter(active=1).order_by('date_created')

    else:
        results = Distributor.objects.filter(active=1).order_by('date_created')
        
    paginator = Paginator(results, 10) # Pagination @ Distributor Models
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = { 'page_obj' : page_obj, 
                'search': form_search
                    }
    return render(request, 'distributor/index.html' , context)

@login_required(login_url='home:process')
def detail(request, distrib_id):
    # request try for id of models.Distributor
    try:
        distrib = Distributor.objects.get(pk=distrib_id)

        # parent and child between Distributor and Brand models get from id @ try
        items = distrib.item_set.all()
        brands = distrib.brand_set.all()

        form_search = Search(request.GET)
        query = request.GET.get('search', '')
            
        if form_search.is_valid():
            results = items.filter(name__icontains=query)

        else:
            results = items.filter(active=1)

        paginator = Paginator(results, 10)  # Paginate the brands with 10 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = { 'distrib': distrib, 
                    'page_obj': page_obj,
                    'search' : form_search,
                    'brands' : brands,
                    }
                 
        return render(request, 'distributor/detail.html', context)
    except Distributor.DoesNotExist:
        raise Http404("User does not exist")