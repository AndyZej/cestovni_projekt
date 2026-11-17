

from django.shortcuts import render
from django.http import Http404

def seznam_itineraru_view(request):
    """Stránka se seznamem itinerářů s ručně definovanými kartami"""
    itinerare = [
        {'nazev': 'Turecko', 'slug': 'turecko'},
        {'nazev': 'Kapverdy', 'slug': 'kapverdy'},
        {'nazev': 'Tunisko', 'slug': 'tunisko'},
        {'nazev': 'Egypt', 'slug': 'egypt'},
    ]
    return render(request, 'itinerar/seznam_itinerar.html', {'itinerare': itinerare})

def detail_itineraru_view(request, slug):
    """Dynamicky otevře HTML šablonu pro itinerář podle slugu"""
    # Sjednoceno na malé písmena podle reálných souborů na disku,
    # aby nedocházelo k chybám na různých operačních systémech
    template_map = {
        'turecko': 'itinerar/itinerar/turecko.html',
        'kapverdy': 'itinerar/itinerar/kapverdy.html',
        'tunisko': 'itinerar/itinerar/tunisko.html',
        'egypt': 'itinerar/itinerar/egypt.html',
    }

    template_name = template_map.get(slug)
    if not template_name:
        raise Http404("Itinerář nebyl nalezen")

    return render(request, template_name)

def kapverdy_itinerar_galerie_view(request):
    return render(request, 'itinerar/galerie/kapverdy.html')

def egypt_itinerar_galerie_view(request):
    return render(request, 'itinerar/galerie/egypt.html')

def tunisko_itinerar_galerie_view(request):
    return render(request, 'itinerar/galerie/tunisko.html')

def turecko_itinerar_galerie_view(request):
    return render(request, 'itinerar/galerie/turecko.html')