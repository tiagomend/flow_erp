from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from WMS.forms import WarehouseTypeForm
from WMS.models import WarehouseType


class CreateWarehouseType(View):
    template = 'wms/w_type_form.html'
    context = {
        'page_name': 'Novo Tipo de Armazém'
    }

    def get(self, request):
        form = WarehouseTypeForm()
        self.context['form'] = form

        return render(request, self.template, self.context)

    def post(self, request):
        form = WarehouseTypeForm(request.POST)

        if form.is_valid():
            w_type = form.save()

            messages.success(request, 'Tipo de Armazém criado com sucesso!')

            return redirect('update_wt', w_type.pk)

        else:
            self.context['form'] = form
            return render(request, self.template, self.context)


class UpdateWarehouseType(View):
    template = 'wms/w_type_form.html'
    context = {}

    def get(self, request, id):
        w_type = WarehouseType.objects.get(pk=id)
        form = WarehouseTypeForm(instance=w_type)
        self.context['form'] = form
        self.context['page_name'] = f'Editar: {w_type}'

        return render(request, self.template, self.context)

    def post(self, request, id):
        w_type = WarehouseType.objects.get(pk=id)
        form = WarehouseTypeForm(request.POST, instance=w_type)

        if form.is_valid():
            form.save()

            messages.success(
                request, f'{w_type} editado com sucesso!')

            self.context['form'] = form
            self.context['page_name'] = f'Editar: {w_type}'
            return render(request, self.template, self.context)

        else:
            self.context['form'] = form
            self.context['page_name'] = f'Editar: {w_type}'
            return render(request, self.template, self.context)


class ReadWarehouseType(View):
    def get(self, request):
        template = 'wms/w_type_list.html'
        w_types = WarehouseType.objects.all().order_by('pk')
        context = {
            'w_types': w_types,
            'page_name': 'Lista de Tipos de Armazém',
        }

        return render(request, template, context)
