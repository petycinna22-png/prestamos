from django.db import models

from django.core.exceptions import ValidationError
# Create your models here.
class Pago(models.Model):
    prestamo = models.ForeignKey(
        "prestamos_app.Prestamo",
        on_delete=models.CASCADE,
        related_name="pagos"
    )

    monto=models.DecimalField(max_digits=10, decimal_places=2)
    fecha=models.DateField()
    nota=models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"Pago {self.monto} - {self.fecha}"
    
    def clean(self):
        if not self.pk:
            # Durante la validación del form, la instancia puede no tener
            # el campo `prestamo` asignado todavía. Evitar acceder al
            # related object hasta que esté disponible.
            if self.prestamo_id is None:
                return
            if self.monto > self.prestamo.saldo_pendiente():
                raise ValidationError("El pago excede al saldo pendiente")
