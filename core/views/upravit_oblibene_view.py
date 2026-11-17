


from core.models import UzivatelskaObdobnaCast
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import NoReverseMatch, reverse

# Struktura: 'klic': ('Název části', 'django_url_name', 'ikona', 'slug_nebo_None')
MAPOVANI_SEKCÍ = {
    # Země a galerie zemí
    'seznam_zemi': ('Všechny země', 'seznam_zemi', '🌍', None),
    'egypt_detail': ('Egypt – Popis země', 'detail_zeme', '🇪🇬', 'egypt'),
    'egypt_galerie': ('Egypt – Galerie země', 'egypt_galerie', '📸', None),
    'kapverdy_detail': (
        'Kapverdy – Popis země',
        'detail_zeme',
        '🇨🇻',
        'kapverdy',
    ),
    'kapverdy_galerie': (
        'Kapverdy – Galerie země',
        'kapverdy_galerie',
        '📸',
        None,
    ),
    'tunisko_detail': (
        'Tunisko – Popis země',
        'detail_zeme',
        '🇹🇳',
        'tunisko',
    ),
    'tunisko_galerie': (
        'Tunisko – Galerie země',
        'tunisko_galerie',
        '📸',
        None,
    ),
    'turecko_detail': (
        'Turecko – Popis země',
        'detail_zeme',
        '🇹🇷',
        'turecko',
    ),
    'turecko_galerie': (
        'Turecko – Galerie země',
        'turecko_galerie',
        '📸',
        None,
    ),
    # Itineráře a galerie itinerářů
    'seznam_itineraru': ('Všechny itineráře', 'seznam_itineraru', '🗺️', None),
    'egypt_itinerar': (
        'Egypt – Itinerář',
        'detail_itineraru',
        '🇪🇬',
        'egypt',
    ),
    'egypt_itinerar_galerie': (
        'Egypt – Galerie itineráře',
        'egypt_itinerar_galerie',
        '📸',
        None,
    ),
    'kapverdy_itinerar': (
        'Kapverdy – Itinerář',
        'detail_itineraru',
        '🇨🇻',
        'kapverdy',
    ),
    'kapverdy_itinerar_galerie': (
        'Kapverdy – Galerie itineráře',
        'kapverdy_itinerar_galerie',
        '📸',
        None,
    ),
    'tunisko_itinerar': (
        'Tunisko – Itinerář',
        'detail_itineraru',
        '🇹🇳',
        'tunisko',
    ),
    'tunisko_itinerar_galerie': (
        'Tunisko – Galerie itineráře',
        'tunisko_itinerar_galerie',
        '📸',
        None,
    ),
    'turecko_itinerar': (
        'Turecko – Itinerář',
        'detail_itineraru',
        '🇹🇷',
        'turecko',
    ),
    'turecko_itinerar_galerie': (
        'Turecko – Galerie itineráře',
        'turecko_itinerar_galerie',
        '📸',
        None,
    ),
    # Komunita a zprávy
    'zpravy_vsechny': ('Všechny diskuze', 'zpravy', '💬', None),
    'komunita_egypt': ('Komunita: Egypt', 'zpravy', '🇪🇬', None),
    'komunita_kapverdy': ('Komunita: Kapverdy', 'zpravy', '🇨🇻', None),
    'komunita_tunisko': ('Komunita: Tunisko', 'zpravy', '🇹🇳', None),
    'komunita_turecko': ('Komunita: Turecko', 'zpravy', '🇹🇷', None),
    'chat_admin': ('Zprávy s administrátorem', 'chat_admin', '✉️', None),
    'domov': ('Domovská stránka', 'domov', '🏠', None),
}


def ziskej_bezpecnou_url(klic):
  """Vygeneruje hotovou URL adresu i s případným slugem a nespadne na NoReverseMatch."""
  if klic not in MAPOVANI_SEKCÍ:
    return '/'
  _, url_name, _, slug = MAPOVANI_SEKCÍ[klic]
  try:
    if slug:
      return reverse(url_name, kwargs={'slug': slug})
    return reverse(url_name)
  except NoReverseMatch:
    # Záložní varianta, pokud by url_name bralo args místo kwargs nebo neexistovalo
    try:
      if slug:
        return reverse(url_name, args=[slug])
    except NoReverseMatch:
      return '/'
    return '/'


@login_required
def upravit_oblibene_view(request):
  if request.method == 'POST':
    vybrane_polozky = request.POST.getlist('oblibene_sekce')[:4]
    UzivatelskaObdobnaCast.objects.filter(uzivatel=request.user).delete()

    for index, klic in enumerate(vybrane_polozky, start=1):
      if klic in MAPOVANI_SEKCÍ:
        nazev, _, ikona, _ = MAPOVANI_SEKCÍ[klic]
        UzivatelskaObdobnaCast.objects.create(
            uzivatel=request.user,
            nazev_casti=nazev,
            url_name=klic,
            ikona=ikona,
            poradi=index,
        )
    return redirect('upravit_oblibene')

  oblibene_sekce = UzivatelskaObdobnaCast.objects.filter(
      uzivatel=request.user
  ).order_by('poradi')

  for sekce in oblibene_sekce:
    sekce.hotova_url = ziskej_bezpecnou_url(sekce.url_name)

  vybrane_klice = [s.url_name for s in oblibene_sekce]
  rozbalit_menu = not oblibene_sekce.exists()

  return render(
      request,
      'core/upravit_oblibene.html',
      {
          'oblibene_sekce': oblibene_sekce,
          'vybrane_klice': vybrane_klice,
          'rozbalit_menu': rozbalit_menu,
      },
  )


@login_required
def dashboard_uctu(request):
  oblibene_sekce = UzivatelskaObdobnaCast.objects.filter(
      uzivatel=request.user
  ).order_by('poradi')

  for sekce in oblibene_sekce:
    sekce.hotova_url = ziskej_bezpecnou_url(sekce.url_name)

  return render(
      request,
      'core/dashboard_uctu.html',
      {
          'oblibene_sekce': oblibene_sekce,
      },
  )