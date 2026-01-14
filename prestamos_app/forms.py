from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        #fields = "__all__"
        widgets = {
            'fecha_inicio': forms.DateInput(
                attrs={'type':'date'}
            )
        }
        fields = ['monto', 'fecha_inicio', 'descripcion']
