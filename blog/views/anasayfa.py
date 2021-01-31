from django.shortcuts import render

def anasayfa(request):
    context = {
        'isim': 'Oğuzhan Çelikarslan'
    }
    return render(request, 'pages/anasayfa.html', context=context)