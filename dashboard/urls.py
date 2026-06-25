from django.urls import path
from .views import dashboard
from .admin_views import admin_dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
]