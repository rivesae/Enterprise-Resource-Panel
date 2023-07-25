from django.urls import path, include
from . import views

app_name = 'distrib'
urlpatterns = [
    path('', views.distributors, name='overview'),
    path('<int:distrib_id>/', views.detail, name='detail'),
]