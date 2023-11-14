from django.db import models


class ItemGroup(models.Model):
    description = models.CharField(max_length=48)

    class Meta:
        db_table = 'item_group'

    def __str__(self) -> str:
        return f'{self.description}'
