


for index, klic in enumerate(vybrane_polozky, start=1):
    if klic in mapovani_nazvu:
        nazev, url_name, ikona = mapovani_nazvu[klic]  # Tady si vytáhneš 'url_name'
        UzivatelskaObdobnaCast.objects.create(
            uzivatel=request.user,
            nazev_casti=nazev,
            url_name=klic,  # <--- TADY UKLÁDÁŠ 'klic' (např. 'egypt_detail') MÍSTO 'url_name'
            ikona=ikona,
            poradi=index
        )