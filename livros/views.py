from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import LivrosForm
from .models import Livros

# Create your views here.


# def index(request):
#     livros = Livros.objects.all().order_by('-data_cadastro')
#     return render(request, "livros/listar.html", {'livros': livros})


# def visualizar(request, id):
#     livro = get_object_or_404(Livros, pk=id)
#     return render(request, "livros/visualizar.html", {'livro': livro})


# def cadastrar(request):
#     if request.method == 'POST':
#         form = LivrosForm(request.POST)
#         if form.is_valid():
#             livro = form.save()
#             return redirect('/')
#     else:
#         form = LivrosForm()
#     return render(request, "livros/cadastrar.html", {'form': form})


# def atualizar(request, id):
#     livro = get_object_or_404(Livros, pk=id)
#     form = LivrosForm(instance=livro)
#     if(request.method == 'POST'):
#         form = LivrosForm(request.POST, instance=livro)
#         if(form.is_valid()):
#             livro.save()
#             return redirect('/')
#         else:
#             return render(request, "livros/atualizar.html", {'form': form, 'livro': livro})
#     else:
#         return render(request, "livros/atualizar.html", {'form': form, 'livro': livro})


# def deletar(request, id):
#     produto = get_object_or_404(Livros, pk=id)
#     produto.delete()
#     messages.success(request, 'Livro deletado')
#     return redirect('/')

# def pesquisar(request, texto):
#     livros = Livros.objects.filter(titulo__like="texto")

#     messages.success(request, 'Livro deletado')
#     return redirect('/')


class LivrosDetailView(DetailView):
    model = Livros
    context_object_name = 'livro'
    template_name = 'livros/visualizar.html'


class IndexView(generic.ListView):
    template_name = 'livros/listar.html'
    context_object_name = 'livros'
    model = Livros

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     query = self.request.GET.get('q', '')
    #     list_user = Livros.objects.filter(titulo__icontains=query) if query != '' else Livros.objects.all()

    #     context['livros'] = query
    #     return context


class LivrosCreateView(CreateView):
    model = Livros
    template_name = 'livros/cadastrar.html'
    fields = ['titulo', 'descricao', 'editora', 'quantidade']
    success_url = '/'


class LivrosUpdateView(UpdateView):
    model = Livros
    template_name = 'livros/atualizar.html'
    fields = ['titulo', 'descricao', 'editora', 'quantidade']
    success_url = '/'


class LivrosDeleteView(DeleteView):
    model = Livros
    success_url = '/'
