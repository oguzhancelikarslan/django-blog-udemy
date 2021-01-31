from django.shortcuts import render, redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel

def iletisim(request):
    form = IletisimForm()

    if request.method == 'POST':
        form = IletisimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anasayfa')

    context = {
        'form': form
    }
    return render(request, 'pages/iletisim.html', context=context)
