from django import forms

from MDM.models import Address
from MDM.bootstrap import INPUT
from MDM.widgets import CustomCheckbox


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['address_type']
        labels = {
            'public_place_type': 'Tipo de Logradouro',
            'public_place': 'Logradouro',
            'number': 'Número',
            'complement': 'Complemento',
            'district': 'Bairro',
            'state': 'Estado',
            'city': 'Cidade',
            'postal_code': 'CEP'
        }

        widgets = {
            'public_place_type': forms.Select(attrs=INPUT),
            'public_place': forms.TextInput(attrs=INPUT),
            'number': forms.TextInput(attrs=INPUT),
            'complement': forms.TextInput(attrs=INPUT),
            'district': forms.TextInput(attrs=INPUT),
            'state': forms.TextInput(attrs=INPUT),
            'city': forms.TextInput(attrs=INPUT),
            'postal_code': forms.TextInput(attrs=INPUT)
        }
