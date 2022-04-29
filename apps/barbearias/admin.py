from django.contrib import admin
from .models import Barbearia, Endereco, Profissionais, Servicos, HorarioFuncionamento, AgendaHorario


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