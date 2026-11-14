


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ZpravaAdminovi, KomunitniZprava
from zeme.models import Zeme

# --- 1. KOMUNITNÍ ZPRÁVY (Uživatelé mezi sebou) ---
def komunita_rozcestnik(request):
    vsechny_zeme = Zeme.objects.all()
    return render(request, 'zpravy/komunita_rozcestnik.html', {'vsechny_zeme': vsechny_zeme})

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
    return render(request, 'zpravy/diskuze_zeme.html', {
        'zeme': vybrana_zeme,
        'zpravy': zpravy
    })

# --- 2. CHAT S ADMINISTRÁTOREM ---
@login_required
def chat_admin(request):
    if request.method == 'POST':
        text_zpravy = request.POST.get('zprava')
        if text_zpravy:
            ZpravaAdminovi.objects.create(uzivatel=request.user, zprava=text_zpravy)
            return redirect('chat_admin')

    zpravy = ZpravaAdminovi.objects.filter(uzivatel=request.user).order_by('-cas_odeslani')
    return render(request, 'zpravy/chat_admin.html', {'zpravy': zpravy})
