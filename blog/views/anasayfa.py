from django.shortcuts import render
from blog.models import YazilarModel
from django.core.paginator import Paginator
from django.db.models import Q

def anasayfa(request):
    sorgu = request.GET.get('sorgu')
    yazilar = YazilarModel.objects.order_by('-id')
    
    if sorgu:
        yazilar = yazilar.filter(
            Q(baslik__icontains=sorgu) |
            Q(icerik__icontains=sorgu)
        ).distinct()
        
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(yazilar, 2)

    return render(request, 'pages/anasayfa.html', context={
        'yazilar': paginator.get_page(sayfa)
    })