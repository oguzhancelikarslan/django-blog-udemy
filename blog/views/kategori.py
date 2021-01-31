from django.shortcuts import render, get_object_or_404
from blog.models import YazilarModel, KategoriModel
from django.core.paginator import Paginator
from django.views.generic import ListView

class KategoriListView(ListView):
    template_name = 'pages/kategori.html'
    context_object_name = 'yazilar'
    paginate_by = 2

    def get_queryset(self):
        kategori = get_object_or_404(KategoriModel, slug=self.kwargs['kategoriSlug'])
        return kategori.yazi.all().order_by('-id')