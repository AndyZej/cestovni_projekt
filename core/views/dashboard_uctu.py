
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import UzivatelskaObdobnaCast

@login_required
def upravit_oblibene_view(request):
    # Zde může uživatel spravovat své oblíbené části
    if request.method == 'POST':
        # Zpracování formuláře pro uložení (lze upravit podle vašich formulářů)
        return redirect('dashboard_uctu')

    oblibene = UzivatelskaObdobnaCast.objects.filter(uzivatel=request.user)
    return render(request, 'core/upravit_oblibene.html', {'oblibene': oblibene})