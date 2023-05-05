from django.db import models
from django.contrib.auth.models import User  
# Create your models here.
class days(models.Model):
    name = models.CharField(("Dia"), max_length=50)

    def __str__(self) -> str:
        return self.name
    
class task(models.Model):
    user = models.ForeignKey(User, verbose_name=("Persona"), on_delete=models.CASCADE)
    name = models.CharField(("Tarea"), max_length=50)
    day = models.ForeignKey(days, verbose_name=("Dia"), on_delete=models.CASCADE)
    checkout = models.BooleanField(("Hecho"), default=False)
    created = models.DateTimeField(("Creado"), auto_now_add=True)
    updated = models.DateTimeField(("Actualizado"), auto_now=True)

    class Meta:
        ordering = ['-updated','-created']

        
    def __str__(self) -> str:
        return self.name

class Messages(models.Model):
    user = models.ForeignKey(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    task = models.ForeignKey(task, verbose_name=("Tarea"), on_delete=models.CASCADE,blank=True)
    body = models.TextField((""))
    created = models.DateTimeField(("Creado"), auto_now_add=True)
    updated = models.DateTimeField(("Actualizado"), auto_now=True)

    def __str__(self) -> str:
        return self.body