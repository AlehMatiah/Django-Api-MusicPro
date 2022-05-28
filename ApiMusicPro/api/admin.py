from django.contrib import admin
from .models import Instrumento, Categoria

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    #list_display = ('idCategoria', 'nombre')
    ordering = ('-idCategoria',)
    search_fields = ('idCategoria', 'nombre',)
    #list_editable = ('nombre',)
    #list_display_links = ('idCategoria', 'nombre')
    

@admin.register(Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('idInstrumento', 'nombre', 'valor', 'stock')
    ordering = ('-idInstrumento',)
    search_fields = ('idInstrumento', 'nombre',)
    #list_editable = ('nombre',)
    list_display_links = ('idInstrumento', 'nombre')

#admin.site.register(Instrumento)
#admin.site.register(Categoria)