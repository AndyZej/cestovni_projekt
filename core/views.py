from django.shortcuts import render
from datetime import datetime

def domovska_stranka(request):
    aktualni_cas = datetime.now()
    return render(request, 'core/domovsky.html', {'aktualni_cas': aktualni_cas})
from django.shortcuts import render

# Create your views here.
