from django.urls import path

from MDM.views import *

urlpatterns = [
    path('', HomeResgistration.as_view(), name='home_registration'),
    path('test/', TestView.as_view()),

    # Unit Of Measuremnt
    path('unidade/', ListUOM.as_view(), name='list_uom'),
    path('unidade/novo/', CreateUOM.as_view(), name='create_uom'),
    path('unidade/editar/<str:id>/', UpdateUOM.as_view(), name='update_uom'),

    # Item Group
    path('item/grupo/', ListItemGroup.as_view(), name='list_item_group'),
    path('item/grupo/novo/', CreateItemGroup.as_view(), name='create_item_group'),
    path(
        'item/grupo/editar/<str:id>/',
        UpdateItemGroup.as_view(),
        name='update_item_group'
    ),
]
