from django.urls import path
from .views import agregarCategoria, agregarInstrumento


urlpatterns = [
    path('agregar_Categoria/', agregarCategoria, name='agregar_Categoria'),
    path('agregar_Instrumento/', agregarInstrumento, name='agregar_Instrumento'),
]