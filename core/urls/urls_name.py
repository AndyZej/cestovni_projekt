


from core.models import UzivatelskaObdobnaCast
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Kompletní seznam všech dostupných sekcí (včetně galerií u zemí i itinerářů)
MAPOVANI_SEKCÍ = {
    # 1. Země a destinace
    'seznam_zemi': ('Všechny země', 'seznam_zemi', '🌍'),
    'egypt_detail': ('Egypt – Popis země', 'detail_zeme', '🇪🇬'),
    'egypt_galerie': ('Egypt – Galerie země', 'egypt_galerie', '📸'),
    'kapverdy_detail': ('Kapverdy – Popis země', 'detail_zeme', '🇨🇻'),
    'kapverdy_galerie': ('Kapverdy – Galerie země', 'kapverdy_galerie', '📸'),
    'tunisko_detail': ('Tunisko – Popis země', 'detail_zeme', '🇹🇳'),
    'tunisko_galerie': ('Tunisko – Galerie země', 'tunisko_galerie', '📸'),
    'turecko_detail': ('Turecko – Popis země', 'detail_zeme', '🇹🇷'),
    'turecko_galerie': ('Turecko – Galerie země', 'turecko_galerie', '📸'),
    # 2. Itineráře cest (včetně galerií itinerářů)
    'seznam_itineraru': ('Všechny itineráře', 'seznam_itineraru', '🗺️'),
    'egypt_itinerar': ('Egypt – Itinerář', 'detail_itineraru', '🇪🇬'),
    'egypt_itinerar_galerie': (
        'Egypt – Galerie itineráře',
        'egypt_itinerar_galerie',
        '📸',
    ),
    'kapverdy_itinerar': ('Kapverdy – Itinerář', 'detail_itineraru', '🇨🇻'),
    'kapverdy_itinerar_galerie': (
        'Kapverdy – Galerie itineráře',
        'kapverdy_itinerar_galerie',
        '📸',
    ),
    'tunisko_itinerar': ('Tunisko – Itinerář', 'detail_itineraru', '🇹🇳'),
    'tunisko_itinerar_galerie': (
        'Tunisko – Galerie itineráře',
        'tunisko_itinerar_galerie',
        '📸',
    ),
    'turecko_itinerar': ('Turecko – Itinerář', 'detail_itineraru', '🇹🇷'),
    'turecko_itinerar_galerie': (
        'Turecko – Galerie itineráře',
        'turecko_itinerar_galerie',
        '📸',
    ),
    # 3. Komunita a zprávy
    'zpravy_vsechny': ('Všechny diskuze', 'zpravy', '💬'),
    'komunita_egypt': ('Komunita: Egypt', 'zpravy', '🇪🇬'),
    'komunita_kapverdy': ('Komunita: Kapverdy', 'zpravy', '🇨🇻'),
    'komunita_tunisko': ('Komunita: Tunisko', 'zpravy', '🇹🇳'),
    'komunita_turecko': ('Komunita: Turecko', 'zpravy', '🇹🇷'),
    'chat_admin': ('Zprávy s administrátorem', 'chat_admin', '✉️'),
    'domov': ('Domovská stránka', 'domov', '🏠'),
}


@login_required
def dashboard_uctu(request):
  # Uložení nového výběru z rozbaleného menu
  if request.method == 'POST':
    vybrane_polozky = request.POST.getlist('oblibene_sekce')[:4]
    UzivatelskaObdobnaCast.objects.filter(uzivatel=request.user).delete()

    for index, klic in enumerate(vybrane_polozky, start=1):
      if klic in MAPOVANI_SEKCÍ:
        nazev, _, ikona = MAPOVANI_SEKCÍ[klic]
        UzivatelskaObdobnaCast.objects.create(
            uzivatel=request.user,
            nazev_casti=nazev,
            url_name=klic,  # Ukládáme přesný unikátní klíč (např. 'tunisko_detail')
            ikona=ikona,
            poradi=index,
        )
    # Po uložení přesměrujeme na čistý dashboard (menu se automaticky sbalí)
    return redirect('dashboard_uctu')

  # Načtení uložených sekcí uživatele z databáze
  oblibene_sekce = UzivatelskaObdobnaCast.objects.filter(
      uzivatel=request.user
  ).order_by('poradi')

  # Doplníme ke každé uložené sekci její reálný Django URL název pro odkaz v šabloně
  for sekce in oblibene_sekce:
    if sekce.url_name in MAPOVANI_SEKCÍ:
      sekce.real_url = MAPOVANI_SEKCÍ[sekce.url_name][1]
    else:
      sekce.real_url = 'domov'

  # Seznam klíčů pro předzaškrtnutí checkboxů při rozbalení menu
  vybrane_klice = [s.url_name for s in oblibene_sekce]

  # Pokud uživatel ještě nemá v DB žádnou sekci, menu se rozbalí automaticky
  rozbalit_menu = not oblibene_sekce.exists()

  context = {
      'oblibene_sekce': oblibene_sekce,
      'vybrane_klice': vybrane_klice,
      'rozbalit_menu': rozbalit_menu,
  }
  return render(request, 'core/dashboard_uctu.html', context)