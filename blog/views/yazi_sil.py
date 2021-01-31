from django.contrib.auth.decorators import login_required
from blog.models import YazilarModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def yazi_sil(request, slug):
    get_object_or_404(YazilarModel, slug=slug, yazar=request.user).delete()
    return redirect('yazilarim')

