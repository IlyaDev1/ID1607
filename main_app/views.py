from django.shortcuts import render
from .models import Links


def index(request):
    links = Links.objects.all()
    return render(request, 'index.html', context={'links': links})
