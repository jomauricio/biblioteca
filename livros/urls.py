from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar/', views.LivrosCreateView.as_view(), name='cadastrar'),
    path('deletar/<int:pk>', views.LivrosDeleteView.as_view(), name='deletar'),
    path('<int:pk>', views.LivrosDetailView.as_view(), name='visualizar'),
    path('atualizar/<int:pk>', views.LivrosUpdateView.as_view(), name='atualizar'),
]
