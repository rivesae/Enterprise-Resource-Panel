from django.urls import path, include
from . import views

app_name = 'people'
urlpatterns = [
    path('', views.user_list, name='user_list'),
]