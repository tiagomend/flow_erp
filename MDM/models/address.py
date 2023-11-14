from django.db import models


class AddressType(models.IntegerChoices):
    DEFAULT = 1
    DELIVERY = 2
    BILLING = 3


class PublicPlaceType(models.IntegerChoices):
    STREET = (1, 'Rua')
    AVENUE = (2, 'Avenida')
    FARM = (3, 'Fazenda')


class Address(models.Model):
    address_type = models.IntegerField(
        choices=AddressType.choices,
        default=AddressType.DEFAULT
    )

    public_place_type = models.IntegerField(
        choices=PublicPlaceType.choices,
        default=PublicPlaceType.STREET
    )

    public_place = models.CharField(max_length=64)
    number = models.CharField(max_length=32)
    complement = models.CharField(max_length=32)
    district = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=14)

    @property
    def public_place_type_display(self):
        return self.get_public_place_type_display()

    def __str__(self) -> str:
        if self.complement:
            return '{0} {1}, {2} {3} - {4} - CEP:{5} - {6} - {7}'.format(
                self.public_place_type_display,
                self.public_place,
                self.number,
                self.complement,
                self.district,
                self.postal_code,
                self.city,
                self.state
            )
        else:
            return '{0} {1}, {2} - {3} - CEP:{4} - {5} - {6}'.format(
                self.public_place_type_display,
                self.public_place,
                self.number,
                self.district,
                self.postal_code,
                self.city,
                self.state
            )
