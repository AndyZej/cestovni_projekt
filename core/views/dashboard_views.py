
from datetime import timedelta
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required  # <--- Důležité pro běžné uživatele
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone


# 1. Administrátorský dashboard (ten už máte)
@staff_member_required
def admin_dashboard(request):
    now = timezone.now()
    seven_days_ago = now - timedelta(days=7)
    today = now.date()

    total_users = User.objects.filter(is_staff=False).count()
    new_users = User.objects.filter(date_joined__gte=seven_days_ago).count()
    active_today = User.objects.filter(last_login__date=today).count()
    unread_messages = 0

    context = {
        'total_users': total_users,
        'new_users': new_users,
        'active_today': active_today,
        'unread_messages': unread_messages,
    }
    return render(request, 'core/admin_dashboard.html', context)


# 2. Uživatelský dashboard (pro sekci "Můj účet", kterou teď stavíme)
@login_required  # Zajišťuje, že sem může vstoupit jen přihlášený uživatel
def dashboard_uctu(request):
    # Zde můžete předat do šablony libovolná data o přihlášeném uživateli
    context = {
        'user': request.user,
    }
    return render(request, 'core/dashboard.html', context)