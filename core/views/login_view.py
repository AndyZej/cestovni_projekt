

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def login_view(request):
  # Pokud už je uživatel přihlášený, pošleme ho rovnou na profil
  if request.user.is_authenticated:
    return redirect('uzivatelsky_profil')

  if request.method == 'POST':
    # AuthenticationForm automaticky vezme data z request.POST
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      # Pokud jsou údaje správné, získáme autentizovaného uživatele
      user = form.get_user()
      # Přihlásíme ho do systému (vytvoří session)
      login(request, user)

      # Přesměrování na uživatelskou stránku / profil po úspěšném přihlášení
      return redirect('uzivatelsky_profil')
  else:
    form = AuthenticationForm()

  # Vykreslí naši přihlášenou HTML šablonu a předá do ní prázdný formulář
  return render(request, 'cesta/k/vase_sablone_prihlaseni.html', {'form': form})