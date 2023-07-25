from django.shortcuts import render
from .models import UserInfo

def userinfo(request):
    userinfo = UserInfo.objects.all()
    context = {'userinfo': userinfo}
    return render(request, 'partials/_navbar.html', context)

def user_list(request):
    user_list = UserInfo.objects.all()
    context = {'user_list': user_list}
    return render(request, 'people/index.html', context)