from django.shortcuts import render
# from django.http import HttpResponse
from .models import pages


def home_f(request):
    all_pages = pages.objects.all()
    context = {
        'pages': all_pages
    }
    return render(request, 'home.html', context)


def about_f(request):
    return render(request, 'pages/about.html')

