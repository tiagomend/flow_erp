from django.views import View
from django.shortcuts import render


class TestView(View):
    def get(self, request):
        return render(request, 'mdm/test.html')
