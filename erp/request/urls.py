from django.urls import path, include, re_path
from . import views

app_name = 'request'
urlpatterns = [
    path('', views.index, name="overview"),
    path('form/', views.create_entry, name='create_entry'),
    path('?order=<uuid:uuid_str>.page.<str:str_distrib>', views.redirect_entry, name='redirect_entry'),
    
    
    path('select/', views.select_item, name='select_item'),
    path('costing/', views.costing, name='costing'),
    path('order/<uuid:uuid_str>/active/<uuid:uuid_str2>/', views.toggle_active, name='toggle_active'),
    path('order/<uuid:uuid_str>/toggle-approve', views.toggle_approve, name='toggle_approve'),
    path('order/<uuid:uuid_str>/delete', views.toggle_deactivate, name='toggle_deactivate'),
    path('order/<uuid:uuid_str>/remarks', views.add_remarks, name='add_remarks'),

    path('?order=<uuid:uuid_str>.page=approval', views.approve, name='approve'),
    path('order/<uuid:uuid_str>/toggle-edit', views.toggle_edit, name='toggle_edit'),

    path('order/<uuid:uuid_str>/submit', views.submit, name='submit'),
    
]