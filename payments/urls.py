from django.urls import path
from .views import deposit, withdraw

urlpatterns = [
    path('deposit/', deposit, name='deposit'),
    path('withdraw/', withdraw, name='withdraw'),
]