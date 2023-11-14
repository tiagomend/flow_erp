from django.test import TestCase
from MDM.models import Address, AddressType, PublicPlaceType


class AddressTestCase(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            address_type=AddressType.DEFAULT,
            public_place_type=PublicPlaceType.STREET,
            public_place='Example Street',
            number='123',
            complement='Apt 1',
            district='Bairro',
            state='Example State',
            city='Example City',
            postal_code='12345-678'
        )

    def test_address_creation(self):
        self.assertEqual(Address.objects.count(), 1)
        created_address = Address.objects.get(id=self.address.id)
        self.assertEqual(
            created_address.address_type,
            AddressType.DEFAULT.value
        )
        self.assertEqual(
            created_address.public_place_type,
            PublicPlaceType.STREET.value
        )
        self.assertEqual(created_address.public_place, 'Example Street')
        self.assertEqual(created_address.number, '123')
        self.assertEqual(created_address.complement, 'Apt 1')
        self.assertEqual(created_address.state, 'Example State')
        self.assertEqual(created_address.city, 'Example City')
        self.assertEqual(created_address.postal_code, '12345-678')
