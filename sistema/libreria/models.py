from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Imagen")
    descripcion = models.TextField(null=True, verbose_name="Descripción")

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
