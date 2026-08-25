from django.contrib import admin
from django.urls import path
from app.views import admin_panel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_panel/', admin_panel, name='admin_panel'),
]