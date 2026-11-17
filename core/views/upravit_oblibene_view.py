


# core/views/upravit_oblibene_view.py
from core.models import UserFavoriteSection  # <--- Opraveno na správný model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


@login_required
def upravit_oblibene_view(request):
  if request.method == 'POST':
    vybrane_polozky = request.POST.getlist('oblibene_sekce')[:4]

    # Smažeme staré výběry uživatele
    UserFavoriteSection.objects.filter(user=request.user).delete()

    mapovani_nazvu = {
        'seznam_zemi': ('Všechny země', 'seznam_zemi', '🌍'),
        'egypt_detail': ('Egypt – Detail', 'egypt_detail', '🇪🇬'),
        'egypt_galerie': ('Egypt – Galerie', 'egypt_galerie', '📸'),
        'kapverdy_detail': ('Kapverdy – Detail', 'kapverdy_detail', '🇨🇻'),
        'kapverdy_galerie': ('Kapverdy – Galerie', 'kapverdy_galerie', '📸'),
        'tunisko_detail': ('Tunisko – Detail', 'tunisko_detail', '🇹🇳'),
        'tunisko_galerie': ('Tunisko – Galerie', 'tunisko_galerie', '📸'),
        'turecko_detail': ('Turecko – Detail', 'turecko_detail', '🇹🇷'),
        'turecko_galerie': ('Turecko – Galerie', 'turecko_galerie', '📸'),
        'seznam_itineraru': ('Všechny itineráře', 'seznam_itineraru', '🗺️'),
        'egypt_itinerar': ('Egypt – Itinerář', 'egypt_itinerar', '🇪🇬'),
        'kapverdy_itinerar': ('Kapverdy – Itinerář', 'kapverdy_itinerar', '🇨🇻'),
        'tunisko_itinerar': ('Tunisko – Itinerář', 'tunisko_itinerar', '🇹🇳'),
        'turecko_itinerar': ('Turecko – Itinerář', 'turecko_itinerar', '🇹🇷'),
        'zpravy_vsechny': ('Všechny diskuze', 'zpravy_vsechny', '💬'),
        'komunita_egypt': ('Komunita: Egypt', 'komunita_egypt', '🇪🇬'),
        'komunita_kapverdy': (
            'Komunita: Kapverdy',
            'komunita_kapverdy',
            '🇨🇻',
        ),
        'komunita_tunisko': ('Komunita: Tunisko', 'komunita_tunisko', '🇹🇳'),
        'komunita_turecko': ('Komunita: Turecko', 'komunita_turecko', '🇹🇷'),
        'chat_admin': ('Zprávy s administrátorem', 'chat_admin', '✉️'),
        'domov': ('Domovská stránka', 'domov', '🏠'),
    }

    for index, klic in enumerate(vybrane_polozky, start=1):
      if klic in mapovani_nazvu:
        nazev, url_name, ikona = mapovani_nazvu[klic]
        UserFavoriteSection.objects.create(
            user=request.user,
            section_key=klic,
            title=nazev,
            url_name=url_name,
            ikona=ikona,
            poradi=index,
        )
    return redirect('dashboard_uctu')

  uzivatelske_vybrane = list(
      UserFavoriteSection.objects.filter(user=request.user).values_list(
          'section_key', flat=True
      )
  )
  context = {'uzivatelske_vybrane': uzivatelske_vybrane}
  return render(request, 'core/upravit_oblibene.html', context)