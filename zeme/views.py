from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Zeme

def vyber_zeme(request):
    vsechny_zeme = Zeme.objects.all()
    return render(request, 'zeme/vyber_zeme.html', {'vsechny_zeme': vsechny_zeme})

def detail_itineraru(request, zeme_id):
    zvolena_zeme = get_object_or_404(Zeme, pk=zeme_id)
    return render(request, 'zeme/itinerar.html', {'zvolena_zeme': zvolena_zeme})
