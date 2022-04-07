from django.forms import ModelForm
from .models import Livros

class LivrosForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'descricao', 'editora', 'quantidade']