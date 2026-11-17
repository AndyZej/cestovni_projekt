from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import UzivatelskaObdobnaCast


@login_required
def upravit_oblibene_view(request):
    # Seznam všech dostupných sekcí na vašem webu, které si uživatel může oblíbit
    dostupne_sekce = [
        {'nazev': 'Seznam zemí', 'url_name': 'seznam_zemi', 'ikona': '🌍'},
        {'nazev': 'Itineráře', 'url_name': 'itinerare', 'ikona': '🗺️'},
        {'nazev': 'Zprávy / Podpora', 'url_name': 'zpravy_domu', 'ikona': '💬'},
        {'nazev': 'Domovská stránka', 'url_name': 'domov', 'ikona': '🏠'},
        # Zde můžete přidat další podle vašich URL jmen
    ]

    if request.method == 'POST':
        # Získáme vybrané URL názvy z formuláře (checkboxy)
        vybrane_url = request.POST.getlist('oblibene_sekce')[:4]  # Omezíme na max 4

        # Smažeme staré oblíbené položky uživatele
        UzivatelskaObdobnaCast.objects.filter(uzivatel=request.user).delete()

        # Uložíme nové vybrané
        for index, url_n in enumerate(vybrane_url, start=1):
            # Najdeme odpovídající data k dané sekci
            sekce_info = next((s for s in dostupne_sekce if s['url_name'] == url_n), None)
            if sekce_info:
                UzivatelskaObdobnaCast.objects.create(
                    uzivatel=request.user,
                    nazev_casti=sekce_info['nazev'],
                    url_name=sekce_info['url_name'],
                    ikona=sekce_info['ikona'],
                    poradi=index
                )
        return redirect('dashboard_uctu')

    # Zjistíme, které uživatel už má aktuálně uložené
    uzivatelske_vybrane = list(
        UzivatelskaObdobnaCast.objects.filter(uzivatel=request.user).values_list('url_name', flat=True))

    context = {
        'dostupne_sekce': dostupne_sekce,
        'uzivatelske_vybrane': uzivatelske_vybrane,
    }
    return render(request, 'core/upravit_oblibene.html', context)