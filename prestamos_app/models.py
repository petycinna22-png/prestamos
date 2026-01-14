from django.db import models

# Create your models here.

class Prestamo(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('pagado', 'Pagado'),
        ('vencido', 'Vencido'),
        ('anulado', 'Anulado'),
    ]
    cliente=models.ForeignKey(
        "clientes.Cliente",
        on_delete=models.CASCADE,
        related_name="prestamos"
    )
    monto=models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio=models.DateField()
    descripcion=models.TextField(blank=True)
    activo=models.BooleanField(default=True)
    estado = models.CharField(
        choices=ESTADO_CHOICES,
        default='activo',
        max_length=10
    )

    def cantidad_pagado(self):
        return sum(p.monto for p in self.pagos.all())
    
    def saldo_pendiente(self):
        return self.monto - self.cantidad_pagado()

    def actualizar_estado(self):
        if self.saldo_pendiente() <= 0:
            self.estado = 'pagado'
        return self.estado

    def __str__(self):
        return f"{self.cliente} - {self.monto}"