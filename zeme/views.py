

from django.shortcuts import render
from django.http import Http404
from .models import Zeme


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
    """Dynamicky otevře HTML šablonu země podle slugu"""
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


def seznam_itineraru_view(request):
    """Stránka se seznamem itinerářů s ručně definovanými kartami"""
    itinerare = [
        {'nazev': 'Turecko', 'slug': 'turecko'},
        {'nazev': 'Kapverdy', 'slug': 'kapverdy'},
        {'nazev': 'Tunisko', 'slug': 'tunisko'},
        {'nazev': 'Egypt', 'slug': 'egypt'},
    ]
    return render(request, 'itinerar/domovsky.html', {'itinerare': itinerare})


from django.shortcuts import render
from django.http import Http404

# --- POHLEDY PRO ZEMĚ ---

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


# Samostatné fotogalerie pro jednotlivé země (sekce Země)
def kapverdy_galerie_view(request):
    return render(request, 'zeme/galerie/kapverdy.html')


def egypt_galerie_view(request):
    return render(request, 'zeme/galerie/egypt.html')


def tunisko_galerie_view(request):
    return render(request, 'zeme/galerie/tunisko.html')


def turecko_galerie_view(request):
    return render(request, 'zeme/galerie/turecko.html')


# --- POHLEDY PRO ITINERÁŘE ---

def detail_itineraru_view(request, slug):
    """Dynamicky otevře HTML šablonu pro itinerář podle slugu"""
    template_map = {
        'turecko': 'itinerar/turecko.html',      # Opraveno (zrušena duplicitní složka)
        'kapverdy': 'itinerar/kapverdy.html',    # Opraveno
        'tunisko': 'itinerar/tunisko.html',      # Opraveno
        'egypt': 'itinerar/egypt.html',          # Opraveno
    }

    template_name = template_map.get(slug)
    if not template_name:
        raise Http404("Itinerář nebyl nalezen")

    return render(request, template_name)

    template_name = template_map.get(slug)
    if not template_name:
        raise Http404("Itinerář nebyl nalezen")

    return render(request, template_name)


# Samostatné fotogalerie pro jednotlivé itineráře (sekce Itinerář)[cite: 1]
def kapverdy_itinerar_galerie_view(request):
    return render(request, 'itinerar/itinerar/galerie/kapverdy.html')


def egypt_itinerar_galerie_view(request):
    return render(request, 'itinerar/itinerar/galerie/egypt.html')


def tunisko_itinerar_galerie_view(request):
    return render(request, 'itinerar/itinerar/galerie/tunisko.html')


def turecko_itinerar_galerie_view(request):
    return render(request, 'itinerar/itinerar/galerie/turecko.html')