from django.urls import path
from apps.loja.views import index,buscar,imagem,filtro,todosprodutos

urlpatterns=[
    path('',index,name='index'),
    path('imagem/<int:foto_id>',imagem,name='imagem'),
    path('buscar',buscar,name='buscar'),
    path('filtro/<str:categoria>',filtro,name='filtro'),
    path('todos/',todosprodutos,name='todos'),
]