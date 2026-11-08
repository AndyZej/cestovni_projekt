


from django.shortcuts import get_object_or_404, render
from .models import Zeme

def domov_view(request):
    """Úvodní domovská stránka"""
    return render(request, 'zeme/domovsky.html')

def galerie_view(request):
    """Stránka fotogalerie"""
    return render(request, 'zeme/galerie.html')

def seznam_zemi_view(request):
    """Seznam všech zemí"""
    zemes = Zeme.objects.all()
    return render(request, 'zeme/seznam_zemi.html', {'zemes': zemes})


def detail_zeme_view(request, slug):
    """Dynamicky otevře HTML šablonu podle názvu slugu (např. turecko.html)"""
    # Převede slug na názvy souborů, které máte ve složce templates/zeme/
    template_map = {
        'turecko': 'zeme/turecko.html',
        'kapverdy': 'zeme/Kapverdy.html',
        'tunisko': 'zeme/tunisko.html',
        'egypt': 'zeme/egypt.html',
    }

    # Vybere správnou šablonu, nebo vrátí egypt.html jako výchozí
    template_name = template_map.get(slug, 'zeme/egypt.html')
    return render(request, template_name)


def seznam_itineraru_view(request):
    """Stránka se seznamem itinerářů s ručně definovanými kartami"""
    # Můžete předat seznam položek přímo do šablony itinerar/domovsky.html
    itinerare = [
        {'nazev': 'Turecko', 'slug': 'turecko'},
        {'nazev': 'Kapverdy', 'slug': 'kapverdy'},
        {'nazev': 'Tunisko', 'slug': 'tunisko'},
        {'nazev': 'Egypt', 'slug': 'egypt'},
    ]
    return render(request, 'itinerar/domovsky.html', {'itinerare': itinerare})


def detail_itineraru_view(request, slug):
    """Dynamicky otevře HTML šablonu pro itinerář podle slugu"""
    template_map = {
        'turecko': 'itinerar/turecko.html',
        'kapverdy': 'itinerar/Kapverdy.html',
        'tunisko': 'itinerar/tunisko.html',
        'egypt': 'itinerar/egypt.html',
    }

    # Vybere správnou šablonu, nebo jako výchozí vezme egypt.html
    template_name = template_map.get(slug, 'itinerar/egypt.html')
    return render(request, template_name)
