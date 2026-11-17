

from core.models import UzivatelskaObdobnaCast
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


@login_required
def upravit_oblibene_view(request):
  # Slovník pro mapování hodnot na lidsky čitelné názvy, url a ikony
  mapovani_nazvu = {
      'seznam_zemi': ('Všechny země', 'seznam_zemi', '🌍'),
      'egypt_detail': ('Egypt – Detail', 'detail_zeme', '🇪🇬'),
      'egypt_galerie': ('Egypt – Galerie', 'egypt_galerie', '📸'),
      'kapverdy_detail': ('Kapverdy – Detail', 'detail_zeme', '🇨🇻'),
      'kapverdy_galerie': ('Kapverdy – Galerie', 'kapverdy_galerie', '📸'),
      'tunisko_detail': ('Tunisko – Detail', 'detail_zeme', '🇹🇳'),
      'tunisko_galerie': ('Tunisko – Galerie', 'tunisko_galerie', '📸'),
      'turecko_detail': ('Turecko – Detail', 'detail_zeme', '🇹🇷'),
      'turecko_galerie': ('Turecko – Galerie', 'turecko_galerie', '📸'),
      'seznam_itineraru': ('Všechny itineráře', 'seznam_itineraru', '🗺️'),
      'egypt_itinerar': ('Egypt – Itinerář', 'detail_itineraru', '🇪🇬'),
      'kapverdy_itinerar': ('Kapverdy – Itinerář', 'detail_itineraru', '🇨🇻'),
      'tunisko_itinerar': ('Tunisko – Itinerář', 'detail_itineraru', '🇹🇳'),
      'turecko_itinerar': ('Turecko – Itinerář', 'detail_itineraru', '🇹🇷'),
      'zpravy_vsechny': ('Všechny diskuze', 'zpravy', '💬'),
      'komunita_egypt': ('Komunita: Egypt', 'zpravy', '🇪🇬'),
      'komunita_kapverdy': ('Komunita: Kapverdy', 'zpravy', '🇨🇻'),
      'komunita_tunisko': ('Komunita: Tunisko', 'zpravy', '🇹🇳'),
      'komunita_turecko': ('Komunita: Turecko', 'zpravy', '🇹🇷'),
      'chat_admin': ('Zprávy s administrátorem', 'chat_admin', '✉️'),
      'domov': ('Domovská stránka', 'domov', '🏠'),
  }

  if request.method == 'POST':
    # Získáme zaškrtnuté položky z formuláře (maximálně 4)
    vybrane_polozky = request.POST.getlist('oblibene_sekce')[:4]

    # Smažeme staré oblíbené záznamy uživatele, aby se přepsaly novými
    UzivatelskaObdobnaCast.objects.filter(uzivatel=request.user).delete()

    for index, klic in enumerate(vybrane_polozky, start=1):
      if klic in mapovani_nazvu:
        nazev, url_name, ikona = mapovani_nazvu[klic]
        UzivatelskaObdobnaCast.objects.create(
            uzivatel=request.user,
            nazev_casti=nazev,
            url_name=url_name,  # Zde byla oprava: bere se skutečný URL název z mapování (např. 'detail_zeme')
            ikona=ikona,
            poradi=index,
        )
    return redirect('dashboard_uctu')

  # Pro GET požadavek: Zjistíme, které položky má uživatel již uloženy, aby se zaškrtly
  # Poznámka: Porovnáváme s klíči v mapování (podle toho, jaké value máte v HTML checkboxech)
  uzivatelske_vybrane = list(
      UzivatelskaObdobnaCast.objects.filter(uzivatel=request.user).values_list(
          'url_name', flat=True
      )
  )

  context = {
      'uzivatelske_vybrane': uzivatelske_vybrane,
      'mapovani_nazvu': mapovani_nazvu,  # Přidáno, abyste mohla šablonu snadno vyrenderovat cyklem
  }
  return render(request, 'core/upravit_oblibene.html', context)


@login_required
def dashboard_uctu(request):
  # Načteme uložené oblíbené části uživatele pro zobrazení v dashboardu
  oblibene_sekce = UzivatelskaObdobnaCast.objects.filter(
      uzivatel=request.user
  ).order_by('poradi')

  context = {
      'oblibene_sekce': oblibene_sekce,
  }
  return render(request, 'core/dashboard_uctu.html', context)