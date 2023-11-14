from django.urls import path

from SCM.views import *

urlpatterns = [
    path('fornecedor/novo/', CreateSupplier.as_view(), name='create_supplier'),
    path('fornecedor/editar/<str:id>/',
         UpdateSupplier.as_view(), name='update_supplier'),
    path('fornecedor/', ReadSupplier.as_view(), name='read_supplier'),
]
