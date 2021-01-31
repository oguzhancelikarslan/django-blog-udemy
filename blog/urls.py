from django.urls import path, include
from blog.views import iletisim, anasayfa

urlpatterns = [
    path('', anasayfa),
    path('iletisim', iletisim),
]
