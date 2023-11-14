from django.test import TestCase
from django import forms
from parameterized import parameterized

from MDM.forms import ItemGroupForm
from MDM.bootstrap import INPUT


class ItemGroupFormTest(TestCase):

    @parameterized.expand([
        ('description', 'Descrição do Grupo de Item'),
    ])
    def test_form_labels(self, field, label):
        form = ItemGroupForm()
        self.assertEqual(form.fields[field].label, label)

    @parameterized.expand([
        ('description', forms.TextInput),
    ])
    def test_form_widgets(self, field, widget):
        form = ItemGroupForm()
        self.assertIsInstance(form.fields[field].widget, widget)

    def test_form_valid_data(self):
        form = ItemGroupForm(data={
            'description': 'Grupo de Itens',
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = ItemGroupForm(data={
            'description': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    @parameterized.expand([
        ('description', INPUT['class']),
    ])
    def test_form_widgets_attrs(self, field, attrs):
        form = ItemGroupForm()
        self.assertEqual(form.fields[field].widget.attrs['class'], attrs)
