from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='produto_list'),
    path('novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('editar/<int:pk>/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('excluir/<int:pk>/', views.ProdutoDeleteView.as_view(), name='produto_delete'),

    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nova/', views.CategoriaCreateView.as_view(), name='categoria_create'),

]