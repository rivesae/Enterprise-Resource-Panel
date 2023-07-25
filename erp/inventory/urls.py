from django.urls import path, include
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.index, name="overview"),

]