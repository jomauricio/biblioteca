from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('<int:id>', views.visualizar, name='visualizar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
]