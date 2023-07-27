from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

# Importing forms
from .forms import OrderForm, ItemForm

# Imported models
from .models import RequestItem, RequestOrder
from distributor.models import Distributor, Item, Brand

def index(request):
    orders = RequestOrder.objects.filter(active=1).filter(date_documented=None)
    print(orders)
    context = {
        'orders' : orders,
               }
    return render(request, 'request/index.html', context)

def create_entry(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created = request.user
            instance = form.save()  # Save the new entry

            var_uuid = instance.id
            var_distrib = instance.distributor
            
            print(var_uuid)
            return redirect('request:redirect_entry', uuid_str=str(var_uuid), str_distrib=var_distrib )
    else:
        form = OrderForm()
    context = {
        'form' : form,
        }
    return render(request, 'request/create.html', context)

# Creating Purchase Orders to Distributors
def redirect_entry(request, uuid_str, str_distrib):
    req_order = RequestOrder.objects.filter(id=uuid_str)
    items = RequestItem.objects.filter(request_order=uuid_str).filter(active=1)
    for main_req in req_order:
        brand_get = Brand.objects.filter(distributor_id=main_req.distributor_id)
        if request.method == 'POST':
            item_value = request.POST['item_value']
            qty_value = request.POST['qty_value']
            cost_value = request.POST['cost_value']
            package = request.POST['package']
            user_create = request.user
            
            print(request.user)
            
            target_instance = RequestItem(item_id=item_value, 
                                          qty=qty_value,
                                          cost=cost_value,
                                          package=package,
                                          request_order_id=uuid_str,
                                          created = user_create,
                                          )
            target_instance.save()
    for item in items:
        item.subtotal = item.qty * item.cost
    
    amount = round(sum(item.subtotal for item in items), 2)
    discount_amount = round((amount * main_req.discount), 2)
    total_amount = amount - discount_amount

    context = {
        'items': items,
        'req_order' : req_order,
        'brand_get' : brand_get,
        'main_req' : main_req,
        'total_amount': total_amount,
        'amount' : amount,
        'discount_amount': discount_amount,
               }
    return render(request, 'request/order/entry.html', context)

# HTMX chained-selection for /order/<int:id>/
def select_item(request):
    brand_get = request.GET.get('brand_get')
    select_item = Item.objects.filter(brand=brand_get)
    context = {
        'select_item': select_item,
        }
    return render(request, 'request/order/_partials/_select_item.html', context)

def costing(request):
    item_id = request.GET.get('item_value')
    try:
        instance = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        pass
    else:
        costing = instance.cost
        package = instance.default_pack

    context = {
        'costing': costing,
        'package': package,
               }
    return render(request, 'request/order/_partials/_costing.html', context)

def toggle_deactivate(request, uuid_str):
    target_instance = get_object_or_404(RequestOrder, id=uuid_str)
    if request.method == 'POST':
        target_instance.sent_to = None
        target_instance.delivery_dated = None
        target_instance.update = timezone.now()
        target_instance.date_deleted = timezone.now()
        target_instance.date_documented = timezone.now()
        target_instance.active = 0
        target_instance.deleted_id = request.user
        target_instance.status = "Deleted"
        target_instance.save()
    return redirect('request:overview')

def add_remarks(request, uuid_str):
    target_instance = get_object_or_404(RequestOrder, id=id)
    if request.method == 'POST':
        remark = request.POST['remarks']
        target_instance.remarks = remark,

        target_instance.save()
    return redirect('request:overview')

# Togglers for /order/<int:id>/
# Deleting items in table
def toggle_active(request, uuid_str, uuid_str2):
    if request.method == 'POST':
        item = RequestItem.objects.get(pk=uuid_str2)
        item.delete_date = timezone.now()
        item.deleted_id = request.user
        item.status = "Undocumented"
        item.active = not item.active
        item.save()
    return redirect('request:redirect_entry', uuid_str, uuid_str2)

# Toggle approve signed with update date
def toggle_approve(request, uuid_str):
    if request.method == 'POST':
        approve = RequestOrder.objects.get(pk=uuid_str)
        approve.update = timezone.now()
        approve.save()
    return redirect('request:overview')

# For Approving a Purchase Order /order/<int:id>/approve
def approve(request, uuid_str):
    req_order = RequestOrder.objects.filter(id=uuid_str)
    items = RequestItem.objects.filter(request_order=uuid_str).filter(active=1)
    for main_req in req_order:
        brand_get = Brand.objects.filter(distributor_id=main_req.distributor_id)

    for item in items:
        item.subtotal = item.qty * item.cost
    
    amount = round(sum(item.subtotal for item in items), 2)
    discount_amount = round((amount * main_req.discount), 2)
    total_amount = amount - discount_amount

    context = {
        'items': items,
        'req_order' : req_order,
        'brand_get' : brand_get,
        'main_req' : main_req,
        'total_amount': total_amount,
        'amount' : amount,
        'discount_amount': discount_amount,
               }
    return render(request, 'request/order/approve.html', context)

# Toggler back to edit /order/<int:id>/
def toggle_edit(request, uuid_str):
    if request.method == 'POST':
        approve = RequestOrder.objects.get(pk=uuid_str)
        approve.update = None
        approve.save()
    return redirect('request:overview')

def submit(request, uuid_str):
    target_instance = get_object_or_404(RequestOrder, id=uuid_str)
    if request.method == 'POST':
        target_instance.update = timezone.now()
        target_instance.date_documented = timezone.now()
        target_instance.approved_id = request.user
        target_instance.status = request.POST['status']
        target_instance.save()
    return redirect('request:overview')