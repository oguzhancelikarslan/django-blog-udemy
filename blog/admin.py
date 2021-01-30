from django.contrib import admin
from blog.models import KategoriModel, YazilarModel

admin.site.register(KategoriModel)


class YazilarAdmin(admin.ModelAdmin):
    search_fields = ('baslik', 'icerik')
    list_display = (
        'baslik', 'olusturulma_tarihi', 'duzenlenme_tarihi'
    )

admin.site.register(YazilarModel, YazilarAdmin)