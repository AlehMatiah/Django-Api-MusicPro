from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200)

    #Mostrar el nombre en Django Admin
    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)

class Instrumento(models.Model):
    idInstrumento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    color  = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200)
    valor = models.IntegerField()
    codigo = models.CharField(max_length=15)
    stock = models.IntegerField()
    Categoria = models.ForeignKey(default=None, to=Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='instrumentos/')

    #Mostrar el nombre en Django Admin
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.Categoria)