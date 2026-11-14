


# views/administrator/administrator.py
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from zpravy.models import ChatMessage


@login_required
def chat_admin(request):
  """Pohled pro zákazníka na webu (připomíná WhatsApp widget / chat s adminem)"""
  admin_user = User.objects.filter(is_superuser=True).first()

  if request.method == 'POST' and admin_user:
    text_zpravy = request.POST.get('zprava') or request.POST.get('message')
    if text_zpravy:
      ChatMessage.objects.create(
          sender=request.user, receiver=admin_user, message=text_zpravy
      )
      return redirect('chat_admin')

  zpravy = (
      ChatMessage.objects.filter(
          Q(sender=request.user, receiver=admin_user)
          | Q(sender=admin_user, receiver=request.user)
      ).order_by('timestamp')
      if admin_user
      else []
  )

  return render(
      request,
      'zpravy/administrator/chat/chat_admin.html',
      {'zpravy': zpravy, 'admin_user': admin_user},
  )


def is_admin(user):
  return user.is_authenticated and user.is_superuser


@user_passes_test(is_admin)
def admin_chat_dashboard_view(request):
  """Centrální administrátorský panel pro správu zpráv od všech uživatelů"""
  aktivni_uzivatele = User.objects.filter(sent_messages__isnull=False).distinct()

  vybrany_uzivatel_id = request.GET.get('user_id')
  aktivni_zpravy = []
  vybrany_uzivatel = None

  if vybrany_uzivatel_id:
    vybrany_uzivatel = get_object_or_404(User, id=vybrany_uzivatel_id)

    if request.method == 'POST':
      text_zpravy = request.POST.get('zprava') or request.POST.get('message')
      if text_zpravy:
        ChatMessage.objects.create(
            sender=request.user, receiver=vybrany_uzivatel, message=text_zpravy
        )
        return redirect(f'{request.path}?user_id={vybrany_uzivatel_id}')

    aktivni_zpravy = ChatMessage.objects.filter(
        Q(sender=request.user, receiver=vybrany_uzivatel)
        | Q(sender=vybrany_uzivatel, receiver=request.user)
    ).order_by('timestamp')

  return render(
      request,
      'zpravy/administrator/chat/admin_dashboard.html',
      {
          'aktivni_uzivatele': aktivni_uzivatele,
          'vybrany_uzivatel': vybrany_uzivatel,
          'aktivni_zpravy': aktivni_zpravy,
      },
  )