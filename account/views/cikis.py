from django.contrib.auth import logout
from django.shortcuts import redirect

def cikis(request):
    logout(request)
    return redirect('anasayfa')