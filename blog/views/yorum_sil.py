from django.contrib.auth.decorators import login_required
from blog.models import YorumModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def yorum_sil(request, id):
    yorum = get_object_or_404(YorumModel, id=id)
    if yorum.yazan == request.user or yorum.yazi.yazar == request.user:
        yorum.delete()
        return redirect('detay', slug=yorum.yazi.slug)

    return redirect('anasayfa')

