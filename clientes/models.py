from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Cliente(models.Model):
    usuario=models.CharField(max_length=10)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    phone_regex=RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El numero debe ser +999999999")
    telefono=models.CharField(validators=[phone_regex],max_length=17)
    direccion=models.TextField(max_length=20, blank=True)
    activo=models.BooleanField(default=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True)

    def total_prestado(self):
        return sum(p.monto for p in self.prestamos.all())
    
    def total_pagado(self):
        return sum(p.cantidad_pagado() for p in self.prestamos.all())    
    
    def total_pendiente(self):
        return self.total_prestado() - self.total_pagado()

    def __str__(self):
        return self.usuario
