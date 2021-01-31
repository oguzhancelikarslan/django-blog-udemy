from django.shortcuts import render

def iletisim(request):
    context = {
        'key': 'başlık içerik naber'
    }
    return render(request, 'pages/iletisim.html', context=context)
