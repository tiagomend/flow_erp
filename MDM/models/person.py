from django.db import models


class DocumentType(models.TextChoices):
    CPF = 'CPF'
    RG = 'RG'
    CNPJ = 'CNPJ'
    IE = 'IE'


class Document(models.Model):
    doc_type = models.CharField(max_length=6, choices=DocumentType.choices)
    doc_number = models.CharField(max_length=20)


class Person(models.Model):
    TYPE = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    person_type = models.CharField(max_length=2, choices=TYPE, default='PJ')
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    documents = models.ManyToManyField(Document)
    adresses = models.ManyToManyField('MDM.Address')

    class Meta:
        abstract = True

    @property
    def cpf_display(self):
        for doc in self.documents.all():
            self.documents.exists()
            if doc.doc_type == 'CPF':
                return doc.doc_number

    @property
    def cpf(self):
        for doc in self.documents.all():
            if doc.doc_type == 'CPF':
                return doc

    @property
    def rg_display(self):
        for doc in self.documents.all():
            if doc.doc_type == 'RG':
                return doc.doc_number

    @property
    def cnpj_display(self):
        for doc in self.documents.all():
            if doc.doc_type == 'CNPJ':
                return doc.doc_number

    @property
    def cnpj(self):
        for doc in self.documents.all():
            if doc.doc_type == 'CNPJ':
                return doc

    @property
    def ie_display(self):
        for doc in self.documents.all():
            if doc.doc_type == 'IE':
                return doc.doc_number

    @property
    def ie(self):
        for doc in self.documents.all():
            if doc.doc_type == 'IE':
                return doc

    @property
    def address(self):
        for address in self.adresses.all():
            if address.address_type == 1:
                return address
            else:
                return 'Não há endereço padrão'

    def __str__(self) -> str:
        return f'{self.cnpj_display} - {self.name}'
