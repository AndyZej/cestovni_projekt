

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import UzivatelskePreference


@login_required
def vybrat_oblibene_sekce(views_self, request):  # nebo standardně def (request):
  # Získáme nebo vytvoříme preferenční záznam pro přihlášeného uživatele
  preference, created = UzivatelskePreference.objects.get_or_create(
      uzivatel=request.user
  )

  if request.method == 'POST':
    # Získání všech zaškrtnutých hodnot z formuláře (pole 'oblibene_sekce')
    zvolene_hodnoty = request.POST.getlist('oblibene_sekce')

    # Ochrana na backendu: Ořízneme seznam na maximálně 4 položky, kdyby uživatel obejit JS
    if len(zvolene_hodnoty) > 4:
      zvolene_hodnoty = zvolene_hodnoty[:4]
      # Zde můžeš případně přidat hlášku pro uživatele: messages.warning(request, 'Lze vybrat maximálně 4 sekce.')

    # Uložení do databáze
    preference.vybrane_sekce = zvolene_hodnoty
    preference.save()

    # Přesměrování zpět do dashboardu (uprav si název URL dle své aplikace)
    return redirect('dashboard_uctu')

  # Pro GET požadavek: předáme aktuálně uložené sekce do šablony
  context = {
      'uzivatelske_vybrane': preference.vybrane_sekce,
  }
  return render(
      request, 'cesty/vyber_oblibenych.html', context
  )  # uprav cestu k šabloně podle sebe