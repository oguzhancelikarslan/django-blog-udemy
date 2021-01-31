from django import forms
from blog.models import YorumModel

class YorumEkleModelForm(forms.ModelForm):
    class Meta:
        model = YorumModel
        fields = ('yorum', )