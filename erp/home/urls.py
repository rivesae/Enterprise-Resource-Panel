from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login_view'),
    path('process', views.process_login, name='process'),
    path('logout', views.process_logout, name='logout'),
    path('settings', views.update_stacked_inline, name='user_settings'),
    path('password/', auth_views.PasswordChangeView.as_view()),
]