


from datetime import datetime
from django.shortcuts import render


def domovska_stranka(request):
  aktualni_cas = datetime.now()
  return render(request, 'core/domovsky.html', {'aktualni_cas': aktualni_cas})


def kontakt(request):
  return render(request, 'core/kontakt.html')