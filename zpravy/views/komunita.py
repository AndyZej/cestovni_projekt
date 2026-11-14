
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import KomunitniZprava
from zeme.models import Zeme

def komunita_rozcestnik(request):
    vsechny_zeme = Zeme.objects.all()
    return render(request, 'zpravy/komunita/komunita_rozcestnik.html', {'vsechny_zeme': vsechny_zeme})

@login_required
def diskuze_zeme(request, slug):
    # Pokusíme se najít zemi podle slugu nebo podle názvu (převedeného na malá písmena)
    # Pokud v DB neexistuje, automaticky ji vytvoříme, aby nikdy nebyla 404 chyba!
    nazev_opraveny = slug.capitalize() # např. 'kapverdy' -> 'Kapverdy'

    vybrana_zeme, created = Zeme.objects.get_or_create(
        slug=slug,
        defaults={'nazev': nazev_opraveny}
    )

    if request.method == 'POST':
        text_zpravy = request.POST.get('text')
        if text_zpravy:
            KomunitniZprava.objects.create(
                zeme=vybrana_zeme,
                uzivatel=request.user,
                text=text_zpravy
            )
            return redirect('diskuze_zeme', slug=slug)

    zpravy = KomunitniZprava.objects.filter(zeme=vybrana_zeme).order_by('-cas_odeslani')
    return render(request, 'zpravy/komunita/diskuze_zeme.html', {
        'zeme': vybrana_zeme,
        'zpravy': zpravy
    })