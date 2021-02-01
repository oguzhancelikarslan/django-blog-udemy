from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import YaziGuncelleFormModel
from blog.models import YazilarModel
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class YaziGuncelleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yazi-guncelle.html'
    fields = ('baslik', 'icerik', 'resim', 'kategoriler')

    def get_object(self):
        yazi = get_object_or_404(
            YazilarModel,
            slug=self.kwargs.get('slug'),
            yazar=self.request.user
        )
        return yazi
    
    def get_success_url(self):
        return reverse('detay', kwargs={
            'slug': self.get_object().slug
        })
