from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from MDM.forms import UnitOfMeasurementForm
from MDM.models import UnitOfMeasurement


class CreateUOM(View):
    template = 'mdm/uom_form.html'
    context = {
        'page_name': 'Nova Unidade de Medida'
    }

    def get(self, request):
        form = UnitOfMeasurementForm()
        self.context['form'] = form

        return render(request, self.template, self.context)

    def post(self, request):
        form = UnitOfMeasurementForm(request.POST)

        if form.is_valid():
            uom = form.save()

            messages.success(request, 'Unidade de Medida criada com sucesso!')

            return redirect('update_uom', uom.pk)

        else:
            self.context['form'] = form
            return render(request, self.template, self.context)


class UpdateUOM(View):
    template = 'mdm/uom_form.html'
    context = {}

    def get(self, request, id):
        uom = UnitOfMeasurement.objects.get(pk=id)
        form = UnitOfMeasurementForm(instance=uom)
        self.context['form'] = form
        self.context['page_name'] = f'Editar: {uom}'

        return render(request, self.template, self.context)

    def post(self, request, id):
        uom = UnitOfMeasurement.objects.get(pk=id)
        form = UnitOfMeasurementForm(request.POST, instance=uom)

        if form.is_valid():
            form.save()

            messages.success(
                request, f'{uom.description} editado com sucesso!')

            self.context['form'] = form
            self.context['page_name'] = f'Editar: {uom}'
            return render(request, self.template, self.context)

        else:
            self.context['form'] = form
            self.context['page_name'] = f'Editar: {uom}'
            return render(request, self.template, self.context)


class ListUOM(View):
    def get(self, request):
        template = 'mdm/list_uom.html'
        uoms = UnitOfMeasurement.objects.all().order_by('pk')
        context = {
            'uoms': uoms,
            'page_name': 'Lista de Unidade de Medidas',
        }

        return render(request, template, context)
