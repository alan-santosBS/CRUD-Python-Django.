from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto
from .models import Produto, Categoria

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'catalogo/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'catalogo/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class ProdutoListView(ListView):
    model = Produto
    template_name = 'catalogo/produto_list.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    template_name = 'catalogo/produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'preco', 'categoria']
    template_name = 'catalogo/produto_form.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'catalogo/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')