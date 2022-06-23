from django.contrib import admin
from .models import Barbearia, Endereco, Profissionais, Servicos, HorarioFuncionamento, AgendaHorario, Clientes
from .models import Produtos, ContaPagar, ContaReceber

@admin.register(Barbearia)
class BarbeariaAdmin(admin.ModelAdmin):
    list_display = ('barbearia', 'nome', 'telefone' , 'usuario')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('barbearia', 'cidade', 'estado')


@admin.register(Profissionais)
class ProfissionaisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'barbearia')


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servicos', 'preco', 'tempo', 'barbearia')



@admin.register(HorarioFuncionamento)
class HorarioFuncionamentoAdmin(admin.ModelAdmin):
    list_display = ('dias_da_semana', 'horario_inicio', 'horario_saida', 'barbearia')


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'barbearia')


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')


@admin.register(ContaPagar)
class ContaPgarAdmin(admin.ModelAdmin):
    list_display = ('conta', 'valor', 'dataVencimento', 'dataCadastro', 'pago')


@admin.register(ContaReceber)
class ContaReceberAdmin(admin.ModelAdmin):
    list_display = ('conta', 'valor', 'dataVencimento', 'dataCadastro', 'pago')