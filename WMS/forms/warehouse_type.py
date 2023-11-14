from django import forms

from WMS.models import WarehouseType
from MDM.bootstrap import INPUT


class WarehouseTypeForm(forms.ModelForm):
    class Meta:
        model = WarehouseType
        fields = '__all__'
        labels = {
            'name': 'Nome do Tipo de Armazém',
            'description': 'Descrição'
        }

        widgets = {
            'name': forms.TextInput(attrs=INPUT),
            'description': forms.Textarea(attrs=INPUT)
        }
