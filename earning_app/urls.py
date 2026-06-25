
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib import admin


def home(request):
    return redirect('/dashboard/')


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('payments/', include('payments.urls')),
    path('investments/', include('investments.urls')),
    path('packages/', include('packages.urls')),
]