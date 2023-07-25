from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required

from .models import Update
from people.models import UserInfo
from .forms import SettingsForm, StackedInLineUserForm

from django.http import HttpResponseRedirect


@login_required
def update_stacked_inline(request):
    user = request.user
    stacked_inline = get_object_or_404(UserInfo, user=user)
    
    if request.method == 'POST':
        stacked_inline_form = StackedInLineUserForm(request.POST, instance=stacked_inline)
        user_form = SettingsForm(request.POST, instance=stacked_inline.user)
        
        if stacked_inline_form.is_valid() and user_form.is_valid():
            stacked_inline_form.save()
            user_form.save()
            # Redirect or display success message
            
    else:
        stacked_inline_form = StackedInLineUserForm(instance=stacked_inline)
        user_form = SettingsForm(instance=stacked_inline.user)
    
    return render(request, 'home/settings.html', {
        'stacked_inline_form': stacked_inline_form,
        'user_form': user_form,
    })

@login_required(login_url='home:process')
def home(request):
    update = Update.objects.order_by('-date_created')
    context = {'update':update}
    return render(request, 'home/index.html', context)

def login_view(request):
    return render(request, 'home/login.html')

def process_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'home/login.html', {
            'error_message' : "Login Failed."
        })

def process_logout(request):
    logout(request)
    return HttpResponseRedirect('login')