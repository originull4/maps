from django.contrib import admin
from django.urls import path
from maps.views import maps_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', maps_view, name='maps'),
]
