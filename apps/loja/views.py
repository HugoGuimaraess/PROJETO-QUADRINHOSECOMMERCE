from django.shortcuts import render,get_object_or_404
from apps.loja.models import Loja
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.



def index(request):
    quadrinhos=Loja.objects.all()
    quadrinhos_disponiveis = quadrinhos.filter(disponivel=True).order_by('data')[:8]
    quadrinhos_prevenda=quadrinhos.filter(prevenda=True)[:4]



    return render(request,'loja/index.html',{'cards':quadrinhos_disponiveis,'cards2':quadrinhos_prevenda})



def imagem(request,foto_id):
    quadrinho = get_object_or_404(Loja,pk=foto_id)







    return render(request,'loja/imagem.html',{'imagem':quadrinho})


def buscar(request):
    quadrinhos=Loja.objects.all().filter(disponivel=True).order_by('data')
    paginator = Paginator(quadrinhos,8)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)

    if 'buscar' in request.GET:
        nome_buscar = request.GET['buscar']
        quadrinhos=Loja.objects.filter(quadrinho__icontains=nome_buscar)
    contador = quadrinhos.count()



    return render(request,'loja/buscar.html',{'cards':quadrinhos,'contador':contador})




def filtro(request,categoria):
    filtro=Loja.objects.filter(categoria=categoria,disponivel=True).order_by('data')
    contador=filtro.count()


    return render(request,'loja/filtro.html',{'cat':filtro,'contador':contador})




def todosprodutos(request):
    todosquadrinhos =Loja.objects.all().filter(disponivel=True).order_by('data')
    paginator = Paginator(todosquadrinhos,6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    quantidade=todosquadrinhos.count()
    context={
        'produtinhos':paged_products,
        'quantidade':quantidade
    }


    return render(request,'loja/todos.html',context)









