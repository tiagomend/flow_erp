from parameterized import parameterized
from django.test import TestCase

from MDM.models import UnitOfMeasurement


class UnitOfMeasurementTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        UnitOfMeasurement.objects.create(
            description='Test Description',
            abbreviation='TST',
            is_integer=True,
            activated=True
        )

    @parameterized.expand([
        ('abbreviation', 3),
        ('description', 50),
    ])
    def test_max_length(self, field, value):
        unit = UnitOfMeasurement.objects.get(id=1)
        max_length = unit._meta.get_field(field).max_length
        self.assertEqual(max_length, value)

    def test_is_integer_display(self):
        unit = UnitOfMeasurement.objects.get(id=1)
        self.assertEqual(unit.is_integer_display, 'Sim')

    def test_activated_display(self):
        unit = UnitOfMeasurement.objects.get(id=1)
        self.assertEqual(unit.activated_display, 'Ativo')

    def test_unique_abbreviation(self):
        with self.assertRaises(Exception):
            UnitOfMeasurement.objects.create(
                description='Test Description 2',
                abbreviation='TST',
                is_integer=False,
                activated=True
            )
