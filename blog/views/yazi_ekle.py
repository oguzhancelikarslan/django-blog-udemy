from django.shortcuts import render, redirect
from blog.forms import YaziEkleModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def yazi_ekle(request):
    form = YaziEkleModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        yazi = form.save(commit=False)
        yazi.yazar = request.user
        yazi.save()
        form.save_m2m()
        return redirect('detay', slug=yazi.slug)    
    return render(request, 'pages/yazi-ekle.html', context={
        'form': form
    })