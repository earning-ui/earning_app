from django.urls import path
from .views import buy_package

urlpatterns = [
    path(
        'buy/<int:package_id>/',
        buy_package,
        name='buy_package'
    ),
]