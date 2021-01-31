from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


@login_required(login_url='/')
def sifre_degistir(request):
    if request.method== 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            kullanici = form.save()
            update_session_auth_hash(request, kullanici)
            messages.success(request, 'Şifre başarıyla güncellendi.')
            return redirect('sifre-degistir')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'pages/sifre-degistir.html', context={
        'form': form
    })