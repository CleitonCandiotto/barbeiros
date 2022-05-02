from django.urls import path

from .views import DashboardView
from .views import ServicosList
from .views import ServicosCreate
from .views import ServicosUpdate
from .views import ServicosDelete

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('servicos/', ServicosList.as_view(), name='servicos'),
    path('criar-servico/', ServicosCreate.as_view(), name='criar_servico'),
    path('editar-servico/<int:pk>/', ServicosUpdate.as_view(), name='editar_servico'),
    path('excluir-servico/<int:pk>/', ServicosDelete.as_view(), name='excluir_servico'),
]