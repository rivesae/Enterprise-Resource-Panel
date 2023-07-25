from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('distrib/', include('distributor.urls')),
    path('inventory/', include('inventory.urls')),
    path('request/', include('request.urls')),
    path('people/', include('people.urls')),
    path('customer/', include('customer.urls')),
]