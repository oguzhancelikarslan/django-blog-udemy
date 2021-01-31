from django import forms
from blog.models import IletisimModel

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim','email', 'mesaj')