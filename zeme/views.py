

from django.shortcuts import render
from django.http import Http404
from .models import Zeme


# --- HLAVNÍ STRÁNKY A SEZNAMY ---

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


def seznam_itineraru_view(request):
    """Stránka se seznamem itinerářů s ručně definovanými kartami"""
    itinerare = [
        {'nazev': 'Turecko', 'slug': 'turecko'},
        {'nazev': 'Kapverdy', 'slug': 'kapverdy'},
        {'nazev': 'Tunisko', 'slug': 'tunisko'},
        {'nazev': 'Egypt', 'slug': 'egypt'},
    ]
    return render(request, 'itinerar/domovsky.html', {'itinerare': itinerare})


# --- POHLEDY PRO ZEMĚ (DETAILY A GALERIE) ---

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


# --- POHLEDY PRO ITINERÁŘE (DETAILY A GALERIE) ---

def detail_itineraru_view(request, slug):
    """Dynamicky otevře HTML šablonu pro itinerář podle slugu"""
    template_map = {
        'turecko': 'itinerar/turecko.html',
        'kapverdy': 'itinerar/kapverdy.html',
        'tunisko': 'itinerar/tunisko.html',
        'egypt': 'itinerar/egypt.html',
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