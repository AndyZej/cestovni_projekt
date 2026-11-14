


from django.shortcuts import render
from django.http import Http404
from ..models import Zeme

def domovsky_view(request):
    """Úvodní domovská stránka"""
    return render(request, 'zeme/domovsky.html')

def galerie_view(request):
    """Stránka hlavní fotogalerie"""
    return render(request, 'zeme/zeme/galerie.html')

def seznam_zemi_view(request):
    """Seznam všech zemí z databáze"""
    vsechny_zeme = Zeme.objects.all()
    return render(request, 'zeme/seznam_zemi.html', {'vsechny_zeme': vsechny_zeme})

def detail_zeme_view(request, slug):
    """Dynamicky otevře HTML šablonu pro zemi podle slugu"""
    template_map = {
        'turecko': 'zeme/zeme/turecko.html',
        'kapverdy': 'zeme/zeme/kapverdy.html',
        'tunisko': 'zeme/zeme/tunisko.html',
        'egypt': 'zeme/zeme/egypt.html',
    }

    template_name = template_map.get(slug)
    if not template_name:
        raise Http404("Země nebyla nalezena")

    return render(request, template_name)

def kapverdy_galerie_view(request):
    return render(request, 'zeme/galerie/kapverdy.html')

def egypt_galerie_view(request):
    return render(request, 'zeme/galerie/egypt.html')

def tunisko_galerie_view(request):
    return render(request, 'zeme/galerie/tunisko.html')

def turecko_galerie_view(request):
    return render(request, 'zeme/galerie/turecko.html')