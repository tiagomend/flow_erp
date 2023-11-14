from django.test import TestCase
from django import forms
from parameterized import parameterized

from MDM.forms import UnitOfMeasurementForm
from MDM.bootstrap import INPUT
from MDM.widgets import CustomCheckbox


class UnitOfMeasurementFormTest(TestCase):

    @parameterized.expand([
        ('description', 'Descrição da Unidade de Medida'),
        ('abbreviation', 'Abreviação da Unidade de Medida'),
        ('is_integer', ''),
        ('activated', ''),
    ])
    def test_form_labels(self, field, label):
        form = UnitOfMeasurementForm()
        self.assertEqual(form.fields[field].label, label)

    @parameterized.expand([
        ('description', forms.TextInput),
        ('abbreviation', forms.TextInput),
        ('is_integer', CustomCheckbox),
        ('activated', CustomCheckbox),
    ])
    def test_form_widgets(self, field, widget):
        form = UnitOfMeasurementForm()
        self.assertIsInstance(form.fields[field].widget, widget)

    def test_form_valid_data(self):
        form = UnitOfMeasurementForm(data={
            'description': 'Unidade',
            'abbreviation': 'UN',
            'is_integer': True,
            'activated': True
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = UnitOfMeasurementForm(data={
            'description': '',
            'abbreviation': 'UN',
            'is_integer': 'invalid',
            'activated': 'invalid'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    @parameterized.expand([
        ('description', INPUT['class']),
        ('abbreviation', INPUT['class']),
    ])
    def test_form_widgets_attrs(self, field, attrs):
        form = UnitOfMeasurementForm()
        self.assertEqual(form.fields[field].widget.attrs['class'], attrs)
