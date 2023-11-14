from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from SCM.models import Supplier
from SCM.forms import SupplierForm
from MDM.models import Document, DocumentType
from MDM.forms import AddressForm


class CreateSupplier(View):
    template = 'scm/supplier_form.html'
    context = {
        'page_name': 'Novo Fornecedor'
    }

    def get(self, request):
        form = SupplierForm()

        address_form = AddressForm()
        self.context['form'] = form
        self.context['address_form'] = address_form

        return render(request, self.template, self.context)

    def post(self, request):
        form = SupplierForm(request.POST)
        address_form = AddressForm(request.POST)

        if form.is_valid():
            supplier = form.save()
            cnpj = Document.objects.create(
                doc_type=DocumentType.CNPJ,
                doc_number=request.POST['cnpj']
            )
            cnpj.save()

            ie = Document.objects.create(
                doc_type=DocumentType.IE,
                doc_number=request.POST['ie']
            )
            ie.save()

            supplier.documents.add(cnpj)
            supplier.documents.add(ie)

            if address_form.is_valid():
                address = address_form.save()

                supplier.adresses.add(address)

            supplier.save()

            messages.success(request, 'Fornecedor registrado com sucesso!')

            return redirect('update_supplier', supplier.pk)

        else:
            self.context['form'] = form
            return render(request, self.template, self.context)


class ReadSupplier(View):
    def get(self, request):
        template = 'scm/list_supplier.html'
        suppliers = Supplier.objects.all().order_by('pk')
        context = {
            'suppliers': suppliers,
            'page_name': 'Lista de Fornecedores',
        }

        return render(request, template, context)


class UpdateSupplier(View):
    template = 'scm/supplier_form.html'
    context = {}

    def get(self, request, id):
        supplier = Supplier.objects.get(pk=id)
        form = SupplierForm(instance=supplier)
        address_form = AddressForm(instance=supplier.address)
        self.context['form'] = form
        self.context['address_form'] = address_form
        self.context['page_name'] = f'Editar fornecedor: {supplier}'

        return render(request, self.template, self.context)

    def post(self, request, id):
        supplier = Supplier.objects.get(pk=id)
        form = SupplierForm(request.POST, instance=supplier)
        address_form = AddressForm(request.POST, instance=supplier.address)

        if form.is_valid():
            supplier = form.save()
            cnpj = supplier.cnpj
            ie = supplier.ie
            cnpj_data = request.POST['cnpj']
            ie_data = request.POST['ie']

            self.update_document(cnpj_data, cnpj, supplier, DocumentType.CNPJ)
            self.update_document(ie_data, ie, supplier, DocumentType.IE)

            supplier.save()
            self.context['form'] = form

            if address_form.is_valid():
                address_form.save()
                self.context['address_form'] = address_form

            self.context['page_name'] = f'Editar: {supplier}'

            messages.success(request, 'Fornecedor editado com sucesso!')

            return render(request, self.template, self.context)

        else:
            self.context['form'] = form
            return render(request, self.template, self.context)

    def update_document(self, data, doc, supplier, doc_type):
        if doc:
            doc.doc_number = data
            doc.save()
        else:
            doc = Document.objects.create(
                doc_type=doc_type,
                doc_number=data
            )
            doc.save()
            supplier.documents.add(doc)
