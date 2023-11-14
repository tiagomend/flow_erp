from django.db import models
from django.core.exceptions import ValidationError


class Item(models.Model):
    ITEM_TYPE_CHOICES = [
        (0, 'Mercadoria para revenda'),
        (1, 'Matéria-prima'),
        (2, 'Embalagem'),
        (3, 'Produto em processo'),
        (4, 'Produto acabado'),
        (5, 'Subproduto'),
        (6, 'Produto intermediário'),
        (7, 'Material de uso e consumo'),
        (8, 'Ativo imobilizado'),
        (9, 'Serviços'),
        (10, 'Outros insumos'),
        (99, 'Outros'),
    ]

    code = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=100)
    item_type = models.IntegerField(choices=ITEM_TYPE_CHOICES)
    uom = models.ForeignKey('UnitOfMeasurement', on_delete=models.PROTECT)
    cost = models.FloatField(default=0.00)
    is_stock = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    disabled = models.BooleanField(default=False)
    stocks = models.ManyToManyField('WMS.Warehouse', through='Stock')

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"

    def toggle_disable(self):
        self.disabled = not self.disabled
        self.save()

    @property
    def cost_display(self) -> str:
        return f"R${self.cost:.2f}"

    @property
    def is_stock_display(self) -> str:
        return 'Sim' if self.is_stock else 'Não'

    @property
    def is_sale_display(self) -> str:
        return 'Sim' if self.is_sale else 'Não'

    @property
    def status_display(self) -> str:
        return 'Ativo' if not self.disabled else 'Inativo'

    def as_dict(self) -> dict:
        item_dict = {
            'id': str(self.id),
            'code': self.code,
            'name': self.name,
            'cost': self.cost_display,
            'is_stock': self.is_stock_display,
            'is_sale': self.is_sale_display,
            'disabled': self.status_display,
            'uom': self.uom.abbreviation,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
        }

        return item_dict

    def update_cost(self, price):
        self.cost = price

    @classmethod
    def get_field_label(cls, field) -> str:
        field_label = {
            'code': 'Código (SKU)',
            'name': 'Nome do Item',
            'cost': 'Preço da Última Aquisição',
            'is_stock': 'Item de Estoque',
            'is_sale': 'Item de Venda',
            'disabled': 'Desativado',
            'uom': 'Unidade de Medida Padrão',
            'suppliers': 'Fornecedores',
            'created_at': 'Data de Registro',
            'updated_at': 'Data de Atualização',
        }

        return field_label.get(field, field)

    def validate_code(self, code=None):
        code = code or self.code
        if len(code) < 4:
            raise ValidationError(
                'O Código (SKU) deve ter pelo menos 4 caracteres.'
            )

        else:
            return True

    def validate_is_stock(self):
        # Validates if the item can be marked as a stock item based on it's type.
        invalid_type = [8, 9]
        if self.item_type in invalid_type and self.is_stock:
            item_type = self.get_item_type_display()
            message = f'{item_type} não pode ser item de estoque.'
            raise ValidationError(message)

    def clean(self) -> None:
        self.validate_code()
        self.validate_is_stock()
        return super().clean()
