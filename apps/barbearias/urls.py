from django.urls import path

from .views import ContaReceberCreate, DashboardView, PerfilView, Agenda
from .views import ContaPagarVisualizar, ContaReceberVisualizar
from .views import ServicosList, ClientesList, ProfissionaisList, ProdutosList, EnderecoList
from .views import ContaPagarList, ContaReceberList, FornecedoresList
from .views import ServicosCreate, ClientesCreate, HorarioFuncionamentoCreate, ProfissionaisCreate
from .views import ProdutosCreate, EnderecoCreate, ContaPagarCreate
from .views import ServicosUpdate, ClientesUpdate, HorarioFuncionamentoUpdate, ProfissionaisUpdate
from .views import ProdutoUpdate, BarbeariaUpdate, EnderecoUpdate, ContaPagarUpdate, ContaReceberUpdate
from .views import ServicosDelete, ClientesDelete, ProfissionalDelete, HorarioFuncionamentoDelete
from .views import EnderecoDelete, Produtodelete, ContaPagarDelete, ContaReceberDelete, FornecedorCreate


urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('agenda/', Agenda.as_view(), name='agenda'),

    path('conta-pagar-v/<int:pk>/', ContaPagarVisualizar.as_view(), name='conta_pagarv'),
    path('conta-receber-v/<int:pk>/', ContaReceberVisualizar.as_view(), name='conta_receberv'),

    path('servicos/', ServicosList.as_view(), name='servicos'),
    path('clientes/', ClientesList.as_view(), name='clientes'),
    path('profissionais/', ProfissionaisList.as_view(), name='profissionais'),
    path('produtos/', ProdutosList.as_view(), name='produtos'),
    path('endereco/', EnderecoList.as_view(), name='endereco'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('conta-pagar/', ContaPagarList.as_view(), name='conta_pagar'),
    path('conta-receber/', ContaReceberList.as_view(), name='conta_receber'),
    path('fornecedores/', FornecedoresList.as_view(), name='fornecedores'),

    path('criar-servico/', ServicosCreate.as_view(), name='criar_servico'),
    path('criar-cliente/', ClientesCreate.as_view(), name='criar_cliente'),
    path('criar-profissional/', ProfissionaisCreate.as_view(), name='criar_profissional'),
    path('criar-horario-atendimento/', HorarioFuncionamentoCreate.as_view(), name='criar_horario'), 
    path('criar-produto/', ProdutosCreate.as_view(), name='criar_produto'),
    path('criar-endereco/', EnderecoCreate.as_view(), name='criar_endereco'),
    path('criar-conta-pagar/', ContaPagarCreate.as_view(), name='criar_conta_pagar'),   
    path('criar-conta-receber/', ContaReceberCreate.as_view(), name='criar_conta_receber'),
    path('criar-fornecedor/', FornecedorCreate.as_view(), name='criar_fornecedor'),

    path('editar-servico/<int:pk>/', ServicosUpdate.as_view(), name='editar_servico'),
    path('editar-cliente/<int:pk>/', ClientesUpdate.as_view(), name='editar_cliente'),
    path('editar-profissional/<int:pk>/', ProfissionaisUpdate.as_view(), name='editar_profissional'),
    path('editar-horario-atendimento/<int:pk>/', HorarioFuncionamentoUpdate.as_view(), name='editar_horario'),
    path('editar-produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar_produto'),
    path('barbearia/<int:pk>/',BarbeariaUpdate.as_view(), name='barbearia'),
    path('editar-endereco/<int:pk>/',EnderecoUpdate.as_view(), name='editar_endereco'),
    path('editar-conta-pagar/<int:pk>/',ContaPagarUpdate.as_view(), name='editar_conta_pagar'),
    path('editar-conta-receber/<int:pk>/',ContaReceberUpdate.as_view(), name='editar_conta_receber'),

    path('excluir-servico/<int:pk>/', ServicosDelete.as_view(), name='excluir_servico'),
    path('excluir-cliente/<int:pk>/', ClientesDelete.as_view(), name='excluir_cliente'),
    path('excluir-profissional/<int:pk>/', ProfissionalDelete.as_view(), name='excluir_profissional'),
    path('excluir-horario-atendimento/<int:pk>/', HorarioFuncionamentoDelete.as_view(), name='excluir_horario'),
    path('excluir-endereco/<int:pk>/', EnderecoDelete.as_view(), name='excluir_endereco'),
    path('excluir-produto/<int:pk>/', Produtodelete.as_view(), name='excluir_produto'),
    path('excluir-conta-pagar/<int:pk>/', ContaPagarDelete.as_view(), name='excluir_conta_pagar'),
    path('excluir-conta-receber/<int:pk>/', ContaReceberDelete.as_view(), name='excluir_conta_receber'),
]