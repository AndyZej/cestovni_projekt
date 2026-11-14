


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import KomunitniZprava
from zeme.models import Zeme

def komunita_rozcestnik(request):
    vsechny_zeme = Zeme.objects.all()
    return render(request, 'zpravy/komunita/komunita_rozcestnik.html', {'vsechny_zeme': vsechny_zeme})

@login_required
def diskuze_zeme(request, slug):
    vybrana_zeme = get_object_or_404(Zeme, slug=slug)

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