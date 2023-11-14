from django import forms

from MDM.models import ItemGroup
from MDM.bootstrap import INPUT


class ItemGroupForm(forms.ModelForm):
    class Meta:
        model = ItemGroup
        fields = '__all__'
        labels = {
            'description': 'Descrição do Grupo de Item',
        }

        widgets = {
            'description': forms.TextInput(attrs=INPUT),
        }
