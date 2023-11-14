from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from MDM.models import ItemGroup
from MDM.forms import ItemGroupForm


class CreateItemGroup(View):
    template = 'mdm/item_group_form.html'
    context = {
        'page_name': 'Novo Grupo de Itens'
    }

    def get(self, request):
        form = ItemGroupForm()
        self.context['form'] = form

        return render(request, self.template, self.context)

    def post(self, request):
        form = ItemGroupForm(request.POST)

        if form.is_valid():
            item_group = form.save()
            messages.success(request, 'Grupo de Itens criado com sucesso!')

            return redirect('update_item_group', item_group.pk)

        else:
            self.context['form'] = form
            return render(request, self.template, self.context)


class UpdateItemGroup(View):
    template = 'mdm/item_group_form.html'
    context = {}

    def get(self, request, id):
        item_group = ItemGroup.objects.get(pk=id)
        form = ItemGroupForm(instance=item_group)
        self.context['form'] = form
        self.context['page_name'] = f'Editar: {item_group}'

        return render(request, self.template, self.context)

    def post(self, request, id):
        item_group = ItemGroup.objects.get(pk=id)
        form = ItemGroupForm(request.POST, instance=item_group)

        if form.is_valid():
            form.save()

            messages.success(
                request, f'{item_group.description} editado com sucesso!')

            self.context['form'] = form
            self.context['page_name'] = f'Editar: {item_group}'
            return render(request, self.template, self.context)

        else:
            self.context['form'] = form
            self.context['page_name'] = f'Editar: {item_group}'
            return render(request, self.template, self.context)


class ListItemGroup(View):
    def get(self, request):
        template = 'mdm/list_item_group.html'
        item_group = ItemGroup.objects.all().order_by('pk')
        context = {
            'table': item_group,
            'page_name': 'Lista de Grupo de Itens',
        }

        return render(request, template, context)
