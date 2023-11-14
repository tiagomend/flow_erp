from django import forms

from SCM.models import Supplier
from MDM.bootstrap import INPUT


class SupplierForm(forms.ModelForm):
    cnpj = forms.CharField(
        max_length=18,
        widget=forms.TextInput(attrs=INPUT),
        label='CNPJ',
    )
    ie = forms.CharField(
        max_length=18,
        widget=forms.TextInput(attrs=INPUT),
        label='Inscrição Estadual'
    )

    def __init__(self, *args, **kwargs):
        super(SupplierForm, self).__init__(*args, **kwargs)
        if self.instance.name:
            self.fields['cnpj'].initial = self.instance.cnpj_display
            self.fields['ie'].initial = self.instance.ie_display

    class Meta:
        model = Supplier
        fields = ['person_type', 'name', 'surname']
        widgets = {
            'person_type': forms.Select(attrs=INPUT),
            'name': forms.TextInput(attrs=INPUT),
            'surname': forms.TextInput(attrs=INPUT),
        }

        labels = {
            'person_type': 'Tipo de Pessoa',
            'name': 'Razão Social',
            'surname': 'Nome Fantasia',
        }


class SupplierNaturalForm(forms.ModelForm):
    cpf = forms.CharField(
        max_length=18,
        widget=forms.TextInput(attrs=INPUT),
        label='CPF'
    )
    rg = forms.CharField(
        max_length=18,
        widget=forms.TextInput(attrs=INPUT),
        label='RG'
    )

    class Meta:
        model = Supplier
        fields = ['person_type', 'name']
        widgets = {
            'person_type': forms.Select(attrs=INPUT),
            'name': forms.TextInput(attrs=INPUT),
        }

        labels = {
            'person_type': 'Tipo de Pessoa',
            'name': 'Nome',
        }
