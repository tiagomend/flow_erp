from django.urls import path

from WMS.views import *

urlpatterns = [
    path('armazem/tipo/novo/', CreateWarehouseType.as_view(), name='create_wt'),
    path('armazem/tipo/editar/<str:id>/',
         UpdateWarehouseType.as_view(), name='update_wt'),
    path('armazem/tipo/', ReadWarehouseType.as_view(), name='read_wt'),
]
