
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def registrace(request):
  """Vlastní pohled pro registraci nového uživatele"""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      # Po úspěšné registraci uživatele rovnou přihlásíme
      login(request, user)
      return redirect('domov')  # Název URL, kam uživatele přesměrovat
  else:
    form = UserCreationForm()

  return render(request, 'core/auth/registrace.html', {'form': form})


def prihlaseni(request):
  """Vlastní pohled pro přihlášení existujícího uživatele"""
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('domov')  # Kam uživatele přesměrovat po přihlášení
  else:
    form = AuthenticationForm()

  return render(request, 'core/auth/prihlaseni.html', {'form': form})


def odhlaseni(request):
  """Pohled pro odhlášení uživatele"""
  logout(request)
  return redirect('domov')