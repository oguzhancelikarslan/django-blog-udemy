from django.urls import path
from account.views import cikis, sifre_degistir, profil_guncelle

urlpatterns = [
    path('cikis', cikis, name='cikis'),
    path('sifre-degistir', sifre_degistir, name='sifre-degistir'),
    path('profil-guncelle', profil_guncelle, name='profil-guncelle'),
]