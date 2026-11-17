
# core/views/dashboard_uctu.py
from core.models import UserFavoriteSection
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard_uctu(request):
    # Načteme uložené oblíbené části uživatele pomocí správného modelu UserFavoriteSection
    oblibene_sekce = UserFavoriteSection.objects.filter(
        user=request.user
    ).order_by('poradi')

    context = {
        'oblibene_sekce': oblibene_sekce,
    }

    # Vracíme šablonu dashboardu (ujisti se, že název odpovídá tvému souboru v templates/core/)
    return render(request, 'core/dashboard.html', context)