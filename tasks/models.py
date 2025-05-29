from django.db import models

# Create your models here.
PRIORIDADES = [
    ('alta', 'Alta'),
    ('media', 'Media'),
    ('baja', 'Baja')
]


class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    completo = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    prioridad = models.CharField(
        max_length=5, choices=PRIORIDADES, default='media')

    def __str__(self):

        return self.nombre
