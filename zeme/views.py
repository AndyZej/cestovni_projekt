


from django.shortcuts import render
from .models import Zeme

def domov_view(request):
    return render(request, 'zeme/index.html')

def login_view(request):
    return render(request, 'prihlaseni.html')

def galerie_view(request):
    vsechny_zeme = Zeme.objects.all()
    return render(request, 'zeme/galerie.html', {'vsechny_zeme': vsechny_zeme})

def egypt_view(request):
    zvolena_zeme = Zeme.objects.filter(slug='egypt').first()
    return render(request, 'zeme/egypt.html', {'zvolena_zeme': zvolena_zeme})

def turecko_view(request):
    zvolena_zeme = Zeme.objects.filter(slug='turecko').first()
    return render(request, 'zeme/turecko.html', {'zvolena_zeme': zvolena_zeme})

def kapverdy_view(request):
    zvolena_zeme = Zeme.objects.filter(slug='kapverdy').first()
    return render(request, 'zeme/Kapverdy.html', {'zvolena_zeme': zvolena_zeme})

def tunisko_view(request):
    zvolena_zeme = Zeme.objects.filter(slug='tunisko').first()
    return render(request, 'zeme/tunisko.html', {'zvolena_zeme': zvolena_zeme})