from django.shortcuts import render

def iletisim(request):
    return render(request, 'pages/iletisim.html', context={})
