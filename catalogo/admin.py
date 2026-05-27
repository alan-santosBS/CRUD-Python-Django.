from django.contrib import admin
from .models import Categoria, Produto

# Registrar os modelos para aparecerem no painel admin
admin.site.register(Categoria)
admin.site.register(Produto)