

from datetime import timedelta
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone


@staff_member_required
def admin_dashboard(request):
    now = timezone.now()
    seven_days_ago = now - timedelta(days=7)
    today = now.date()

    total_users = User.objects.filter(is_staff=False).count()
    new_users = User.objects.filter(date_joined__gte=seven_days_ago).count()
    active_today = User.objects.filter(last_login__date=today).count()
    unread_messages = 0

    users_list = User.objects.filter(is_staff=False).order_by('-date_joined')

    context = {
        'total_users': total_users,
        'new_users': new_users,
        'active_today': active_today,
        'unread_messages': unread_messages,
        'users_list': users_list,
    }
    return render(request, 'core/admin_dashboard.html', context)