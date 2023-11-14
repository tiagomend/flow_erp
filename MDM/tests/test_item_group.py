from django.test import TestCase
from MDM.models import ItemGroup


class ItemGroupTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ItemGroup.objects.create(description='Impressora')

    def test_item_group_description(self):
        item_group = ItemGroup.objects.get(id=1)
        self.assertEqual(item_group.description, 'Impressora')

    def test_item_group_str_representation(self):
        item_group = ItemGroup.objects.get(id=1)
        self.assertEqual(str(item_group), 'Impressora')
