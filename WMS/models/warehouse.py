from django.db import models
# from django.contrib.auth.models import User


class Warehouse(models.Model):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    w_type = models.ForeignKey('WarehouseType', on_delete=models.PROTECT)
    address = models.ForeignKey(
        'MDM.Address', on_delete=models.PROTECT, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    disabled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"

    @property
    def address_display(self):
        return '' if self.address is None else self.address
