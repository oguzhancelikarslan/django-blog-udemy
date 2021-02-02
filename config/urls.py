from django.contrib import admin
from django.urls import path, include
from blog.views import iletisim
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('o-admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)