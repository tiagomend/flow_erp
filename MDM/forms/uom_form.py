from django import forms

from MDM.models import UnitOfMeasurement
from MDM.bootstrap import INPUT, CHECKBOX
from MDM.widgets import CustomCheckbox


class UnitOfMeasurementForm(forms.ModelForm):
    class Meta:
        model = UnitOfMeasurement
        fields = '__all__'
        labels = {
            'description': 'Descrição da Unidade de Medida',
            'abbreviation': 'Abreviação da Unidade de Medida',
            'is_integer': '',
            'activated': ''
        }

        widgets = {
            'description': forms.TextInput(attrs=INPUT),
            'abbreviation': forms.TextInput(attrs=INPUT),
            'is_integer': CustomCheckbox(label='Não permitir números fracionados'),
            'activated': CustomCheckbox(label='Ativado'),
        }
