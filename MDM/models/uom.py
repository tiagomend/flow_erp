from django.db import models


class UnitOfMeasurement(models.Model):
    description = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=3, unique=True)
    is_integer = models.BooleanField()
    activated = models.BooleanField(default=True)

    class Meta:
        db_table = 'UOM'

    def __str__(self) -> str:
        return f"{self.abbreviation}"

    @property
    def is_integer_display(self) -> str:
        return 'Sim' if self.is_integer else 'Não'

    @property
    def activated_display(self) -> str:
        return 'Ativo' if self.activated else 'Inativo'
