from django import forms
from .models import SubirDumentoImagen


class SubirDumentoImagenForm(forms.ModelForm):
    class Meta:
        model = SubirDumentoImagen
        fields = ('documento', 'imagen')

    """
    La función __init__ en Python es un método especial que se llama cuando se crea una instancia de una clase. 
    para este caso, sirve para personalizar la inicialización de la instancia del formulario.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['documento'].widget.attrs.update(
            {'accept': '.pdf, .doc, .docx, .txt'})  # Permitir documentos
        self.fields['imagen'].widget.attrs.update(
            {'accept': '.jpg, .jpeg, .png, .gif'})  # Permitir imágenes
