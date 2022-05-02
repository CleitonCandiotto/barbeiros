from django.urls import path

from .views import DashboardView
from .views import ServicosList, ClientesList
from .views import ServicosCreate, ClientesCreate, HorarioFuncionamentoCreate
from .views import ServicosUpdate, ClientesUpdate
from .views import ServicosDelete, ClientesDelete

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('servicos/', ServicosList.as_view(), name='servicos'),
    path('clientes/', ClientesList.as_view(), name='clientes'),

    path('criar-servico/', ServicosCreate.as_view(), name='criar_servico'),
    path('criar-cliente/', ClientesCreate.as_view(), name='criar_cliente'),
    path('criar-horario-atendimento/', HorarioFuncionamentoCreate.as_view(), name='criar_horario'),    

    path('editar-servico/<int:pk>/', ServicosUpdate.as_view(), name='editar_servico'),
    path('editar-cliente/<int:pk>/', ClientesUpdate.as_view(), name='editar_cliente'),

    path('excluir-servico/<int:pk>/', ServicosDelete.as_view(), name='excluir_servico'),
    path('excluir-cliente/<int:pk>/', ClientesDelete.as_view(), name='excluir_cliente'),

]