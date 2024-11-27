from django.contrib import admin
from apps.loja.models import Loja
# Register your models here.


class ListandoLoja(admin.ModelAdmin):
    search_fields = ('quadrinho',),
    list_display = ('id','quadrinho','disponivel','categoria','preco','stock','prevenda',)
    list_display_links = ('id','quadrinho',)
    list_filter = ('categoria',)
    list_editable = ('disponivel','prevenda')
    list_per_page = (10)












admin.site.register(Loja,ListandoLoja)
