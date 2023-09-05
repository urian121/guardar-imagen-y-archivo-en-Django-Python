from django import forms
from .models import SubirDumentoImagen


class SubirDumentoImagenForm(forms.ModelForm):
    class Meta:
        model = SubirDumentoImagen
        fields = ('documento', 'imagen')
