from django.views import View
from django.shortcuts import render


class HomeResgistration(View):
    template = 'mdm/home_registration.html'

    def get(self, request):
        context = {
            'page_name': 'Módulo de Cadastro'
        }

        return render(request, self.template, context)
