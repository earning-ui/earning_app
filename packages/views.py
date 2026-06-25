from django.shortcuts import render
from .models import Package


def package_list(request):

    packages = Package.objects.all()

    return render(
        request,
        'packages/package_list.html',
        {
            'packages': packages
        }
    )