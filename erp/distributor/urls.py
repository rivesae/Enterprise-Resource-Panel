from django.urls import path, include
from . import views

app_name = 'distrib'
urlpatterns = [
    path('', views.distributors, name='overview'),
    path('<uuid:uuid_str>', views.detail, name='detail'),
]