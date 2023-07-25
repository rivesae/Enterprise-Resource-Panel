from django.urls import path, include, re_path
from . import views

app_name = 'request'
urlpatterns = [
    path('', views.index, name="overview"),
    path('form/', views.create_entry, name='create_entry'),
    path('order/<int:id>/', views.redirect_entry, name='redirect_entry'),
    path('select/', views.select_item, name='select_item'),
    path('costing/', views.costing, name='costing'),
    path('order/<int:id>/active/<int:x_id>/', views.toggle_active, name='toggle_active'),
    path('order/<int:id>/toggle-approve', views.toggle_approve, name='toggle_approve'),
    path('order/<int:id>/delete', views.toggle_deactivate, name='toggle_deactivate'),
    path('order/<int:id>/remarks', views.add_remarks, name='add_remarks'),

    path('order/<int:id>/approve', views.approve, name='approve'),
    path('order/<int:id>/toggle-edit', views.toggle_edit, name='toggle_edit'),

    path('order/<int:id>/submit', views.submit, name='submit'),
    
]