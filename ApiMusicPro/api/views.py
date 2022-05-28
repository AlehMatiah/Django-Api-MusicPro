from django.shortcuts import redirect, render
from .forms import CategoriaForm, InstrumentoForm

# Create your views here.

#Página principal
def Home(request):
    return render(request, 'index.html')


    #METODO PARA AGREGAR UNA CATEGORIA
def agregarCategoria(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect('index')
    else:
        categoria_form = CategoriaForm()
    return render(request, 'agregarCategoria.html', {'categoria_form': categoria_form})

    #METODO PARA AGREGAR UN INSTRUMENTO
def agregarInstrumento(request):
    if request.method == 'POST':
        instrumento_form = InstrumentoForm(request.POST)
        if instrumento_form.is_valid():
            instrumento_form.save()
            return redirect('index')
    else:
        instrumento_form = InstrumentoForm()
    return render(request, 'agregarInstrumento.html', {'instrumento_form': instrumento_form})

