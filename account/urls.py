from django.urls import path
from account.views import cikis, sifre_degistir

urlpatterns = [
    path('cikis', cikis, name='cikis'),
    path('sifre-degistir', sifre_degistir, name='sifre-degistir'),
]