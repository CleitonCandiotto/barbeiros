from django.urls import path

from .views import DashboardView, PerfilView
from .views import ServicosList, ClientesList, ProfissionaisList, ProdutosList, EnderecoList
from .views import ServicosCreate, ClientesCreate, HorarioFuncionamentoCreate, ProfissionaisCreate
from .views import ProdutosCreate, EnderecoCreate
from .views import ServicosUpdate, ClientesUpdate, HorarioFuncionamentoUpdate, ProfissionaisUpdate
from .views import ProdutoUpdate, BarbeariaUpdate, EnderecoUpdate
from .views import ServicosDelete, ClientesDelete, ProfissionalDelete, HorarioFuncionamentoDelete
from .views import EnderecoDelete, Produtodelete


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('servicos/', ServicosList.as_view(), name='servicos'),
    path('clientes/', ClientesList.as_view(), name='clientes'),
    path('profissionais/', ProfissionaisList.as_view(), name='profissionais'),
    path('produtos/', ProdutosList.as_view(), name='produtos'),
    path('endereco/', EnderecoList.as_view(), name='endereco'),
    path('perfil/', PerfilView.as_view(), name='perfil'),

    path('criar-servico/', ServicosCreate.as_view(), name='criar_servico'),
    path('criar-cliente/', ClientesCreate.as_view(), name='criar_cliente'),
    path('criar-profissional/', ProfissionaisCreate.as_view(), name='criar_profissional'),
    path('criar-horario-atendimento/', HorarioFuncionamentoCreate.as_view(), name='criar_horario'), 
    path('criar-produto/', ProdutosCreate.as_view(), name='criar_produto'),
    path('criar-endereco/', EnderecoCreate.as_view(), name='criar_endereco'),       
       
    path('editar-servico/<int:pk>/', ServicosUpdate.as_view(), name='editar_servico'),
    path('editar-cliente/<int:pk>/', ClientesUpdate.as_view(), name='editar_cliente'),
    path('editar-profissional/<int:pk>/', ProfissionaisUpdate.as_view(), name='editar_profissional'),
    path('editar-horario-atendimento/<int:pk>/', HorarioFuncionamentoUpdate.as_view(), name='editar_horario'),
    path('editar-produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar_produto'),
    path('barbearia/<int:pk>/',BarbeariaUpdate.as_view(), name='barbearia'),
    path('editar-endereco/<int:pk>/',EnderecoUpdate.as_view(), name='editar_endereco'),

    path('excluir-servico/<int:pk>/', ServicosDelete.as_view(), name='excluir_servico'),
    path('excluir-cliente/<int:pk>/', ClientesDelete.as_view(), name='excluir_cliente'),
    path('excluir-profissional/<int:pk>/', ProfissionalDelete.as_view(), name='excluir_profissional'),
    path('excluir-horario-atendimento/<int:pk>/', HorarioFuncionamentoDelete.as_view(), name='excluir_horario'),
    path('excluir-endereco/<int:pk>/', EnderecoDelete.as_view(), name='excluir_endereco'),
    path('excluir-produto/<int:pk>/', Produtodelete.as_view(), name='excluir_produto'),
]