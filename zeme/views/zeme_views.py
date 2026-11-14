



from django.shortcuts import render
from django.http import Http404
from ..models import Zeme

def domovsky_view(request):
    """Úvodní domovská stránka"""
    return render(request, 'zeme/domovsky.html')

def galerie_view(request):
    """Stránka hlavní fotogalerie"""
    return render(request, 'zeme/galerie.html')

def seznam_zemi_view(request):
    """Seznam všech zemí z databáze"""
    zemes = Zeme.objects.all()
    return render(request, 'zeme/seznam_zemi.html', {'zemes': zemes})

def detail_zeme_view(request, slug):
    """Dynamicky otevře HTML šablonu pro zemi podle slugu"""
    template_map = {
        'turecko': 'zeme/turecko.html',
        'kapverdy': 'zeme/Kapverdy.html',
        'tunisko': 'zeme/tunisko.html',
        'egypt': 'zeme/egypt.html',
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
