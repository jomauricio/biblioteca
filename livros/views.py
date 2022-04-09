from django.shortcuts import render
from django.contrib import messages
from .models import Livros
from .forms import LivrosForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def index(request):
    livros = Livros.objects.all().order_by('-data_cadastro')
    return render(request,"livros/listar.html", {'livros': livros})


def visualizar(request, id):
    livro = get_object_or_404(Livros, pk=id)
    return render(request,"livros/visualizar.html", {'livro': livro})


def cadastrar(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            produto = form.save()
            return redirect('/')
    else:
        form = LivrosForm()
    return render(request, "livros/cadastrar.html", {'form': form} )


def atualizar(request, id):
    livro = get_object_or_404(Livros, pk=id)
    form = LivrosForm(instance=livro)
    if(request.method == 'POST'):
        form = LivrosForm(request.POST, instance = livro)
        if(form.is_valid()):
            livro.save()
            return redirect('/')
        else:
            return render(request, "livros/atualizar.html", {'form':form, 'livro': livro})
    else:
        return render(request, "livros/atualizar.html", {'form':form, 'livro': livro})


def deletar(request, id):
    produto = get_object_or_404(Livros, pk=id)
    produto.delete()
    messages.success(request, 'Livro deletado')
    return redirect('/')

# def pesquisar(request, texto):
#     livros = Livros.objects.filter(titulo__like="texto")
    
#     messages.success(request, 'Livro deletado')
#     return redirect('/')