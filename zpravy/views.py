from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ZpravaAdminovi


@login_required
def chat_admin(request):
    if request.method == 'POST':
        text_zpravy = request.POST.get('zprava')
        if text_zpravy:
            ZpravaAdminovi.objects.create(uzivatel=request.user, zprava=text_zpravy)
            return redirect('chat_admin')

    zpravy = ZpravaAdminovi.objects.filter(uzivatel=request.user).order_by('-cas_odeslani')
    return render(request, 'zpravy/chat_admin.html', {'zpravy': zpravy})
