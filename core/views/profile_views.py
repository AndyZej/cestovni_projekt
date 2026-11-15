
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def uzivatelsky_profil_view(request):
  """Zobrazení uživatelského profilu a správa údajů"""
  if request.method == 'POST':
    # Zde můžete případně zpracovat vlastní POST požadavky (např. změnu údajů)
    pass

  context = {
      'user': request.user,
  }
  return render(request, 'core/profil.html', context)