from django import forms

from .models import Categoria, Instrumento

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['nombre', 'marca', 'color', 'descripcion', 'valor', 'codigo', 'stock', 'Categoria', 'imagen']