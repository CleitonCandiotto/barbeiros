from xml.sax.handler import property_interning_dict
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Servicos, Clientes, HorarioFuncionamento, Profissionais, Produtos, Barbearia, Endereco
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ServicosModelForm, ClienteModelForm,  ProdutosModelForm, ProfissionaisModelForm, HorarioModelForm


class DashboardView(TemplateView):
    template_name = 'dashboard.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        barbearia = Barbearia.objects.filter(usuario=self.request.user).values_list()
        
        if barbearia[0][1] == ' ':
            barbearia = None
        else:
            barbearia = Barbearia.objects.filter(usuario=self.request.user)

        context['clientes'] = Clientes.objects.filter(barbearia=self.request.user.barbearia).count()
        context['barbearia'] = barbearia
        context['endereco'] = Endereco.objects.filter(barbearia=self.request.user.barbearia)
        context['horario'] = HorarioFuncionamento.objects.filter(barbearia=self.request.user.barbearia)
        context['profissionais'] = Profissionais.objects.filter(barbearia=self.request.user.barbearia)

        return context


class PerfilView(TemplateView):
    template_name = 'perfil.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['endereco'] = Endereco.objects.filter(barbearia=self.request.user.barbearia)
        
        return context


# list

class ServicosList(LoginRequiredMixin, ListView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'servicos.html'
    #paginate_by = 10


    def get_queryset(self):
        buscaServico = self.request.GET.get('servico')

        if buscaServico:
            self.object_list = Servicos.objects.filter(
                servicos__icontains=buscaServico,
                barbearia = self.request.user.barbearia
            )
        else:
            self.object_list = Servicos.objects.filter(
                barbearia=self.request.user.barbearia
                )

        return self.object_list


class ClientesList(LoginRequiredMixin, ListView):
    model = Clientes
    login_url = reverse_lazy('login')
    template_name = 'clientes.html'
    paginate_by = 10


    def get_queryset(self):
        '''Pesquisa os clientes por nome ou por qualquer letra'''

        buscaCliente = self.request.GET.get('cliente')

        if buscaCliente:
            self.object_list= Clientes.objects.filter(
                nome__icontains=buscaCliente, 
                barbearia=self.request.user.barbearia
                )
        else:
            self.object_list = Clientes.objects.filter(
                barbearia=self.request.user.barbearia
                )

        return self.object_list


class ProfissionaisList(LoginRequiredMixin, ListView):
    model = Profissionais
    login_url = reverse_lazy('login')
    template_name = 'profissionais.html'


    def get_queryset(self):
        '''Pesquisa os profissionais por nome ou por qualquer letra'''

        buscaProfissional = self.request.GET.get('profissional')

        if buscaProfissional:
            self.object_list = Profissionais.objects.filter(
                nome__icontains=buscaProfissional, 
                barbearia=self.request.user.barbearia
                )
        else:        
            self.object_list = Profissionais.objects.filter(
                barbearia=self.request.user.barbearia
                )
        return self.object_list


class ProdutosList(LoginRequiredMixin, ListView):
    model = Produtos
    login_url = reverse_lazy('login')
    template_name = 'produtos.html'


    def get_queryset(self):
        buscaProduto = self.request.GET.get('produto')

        if buscaProduto:
            self.object_list = Produtos.objects.filter(
                nome__icontains=buscaProduto, 
                barbearia=self.request.user.barbearia
                )
                
        else:
            self.object_list = Produtos.objects.filter(
                barbearia=self.request.user.barbearia
                )
        return self.object_list


class EnderecoList(LoginRequiredMixin, ListView):
    model = Endereco
    login_url = reverse_lazy('login')
    template_name = 'endereco.html'


    def get_queryset(self):
        self.object_list = Endereco.objects.filter(barbearia=self.request.user.barbearia)
        return self.object_list


# create


class ServicosCreate(LoginRequiredMixin, CreateView):
    form_class = ServicosModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_criar/criar_servicos.html'
    success_url = reverse_lazy('servicos')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Serviço'
        context['btn'] = 'Cadastrar'
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        servico = self.request.POST.get('servicos')
        servico_db = Servicos.objects.filter(servicos=servico)
    
        if not servico_db:
            if form.is_valid():
                form.instance.barbearia = self.request.user.barbearia
                messages.success(request, f'Servico: {servico} criado com sucesso')
                form.save()
                return redirect('servicos')
        else:
            messages.warning(request, f'Servico: {servico} ja cadastrado')
            return redirect('servicos')
                  

class ClientesCreate(LoginRequiredMixin, CreateView):
    model = Clientes
    form_class = ClienteModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_criar/criar_clientes.html'
    success_url = reverse_lazy('clientes')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Cliente'
        context['btn'] = 'Cadastrar'
        return context
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        cliente = self.request.POST.get('nome')
        telefone = self.request.POST.get('telefone')
        cliente_db = Clientes.objects.filter(nome=cliente)

        if not cliente_db and len(telefone) > 13:
            if form.is_valid():
                form.instance.barbearia = self.request.user.barbearia
                messages.success(request, f'Cliente: {cliente} cadastrado com sucesso')
                form.save()
                return redirect('clientes')
        
        elif len(telefone) < 13:
            messages.warning(request, 'Telefone invalido')
            return redirect('clientes')

        else:
            messages.warning(request, 'Cliente ja cadastrado')
            return redirect('clientes')


class ProfissionaisCreate(LoginRequiredMixin, CreateView):
    model = Profissionais
    form_class = ProfissionaisModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_criar/criar_profissionais.html'
    success_url = reverse_lazy('profissionais')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Profissional'
        context['btn'] = 'Cadastrar'
        return context
    
    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia
        profissional = Profissionais.objects.filter(nome=form.instance.nome)
        telefone = form.instance.telefone

        if not profissional and len(telefone) > 13:
            messages.success(self.request, f'Profissiononal {profissional} cadastrado com sucesso')
            return super().form_valid(form)
        
        elif len(telefone) < 13:
            messages.warning(self.request, 'Telefone inválido')
            return HttpResponseRedirect(reverse_lazy('profissionais'))

        else:
            messages.warning(self.request, 'Profissional ja cadastrado')
            return HttpResponseRedirect(reverse_lazy('profissionais'))


class HorarioFuncionamentoCreate(LoginRequiredMixin, CreateView):
    model = HorarioFuncionamento
    login_url = reverse_lazy('login')
    form_class = HorarioModelForm
    template_name = 'horario_atendimento.html'
    success_url = reverse_lazy('criar_horario')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horário de Funcionamento'
        context['btn'] = 'Cadastrar'
        context['dias'] = HorarioFuncionamento.objects.filter(barbearia=self.request.user.barbearia)
        return context   


    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        barbearia = self.request.user.barbearia
        diasSemana = self.request.POST.get('dias_da_semana')
        horaInicio = self.request.POST.get('horario_inicio')
        horarioSaida = self.request.POST.get('horario_saida')
        inicioIntervalo = self.request.POST.get('inicio_intervalo')
        finalIntervalo = self.request.POST.get('final_intervalo')
        dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

        if form.is_valid():
            if diasSemana == 'Segunda a Sábado': 
                for dia in dias:
                    hora = HorarioFuncionamento()
                    hora.dias_da_semana = dia
                    hora.horario_inicio = horaInicio
                    hora.horario_saida = horarioSaida
                    hora.inicio_intervalo = inicioIntervalo
                    hora.final_intervalo = finalIntervalo
                    hora.barbearia = barbearia
                    hora.save()
    
                return redirect('criar_horario')

            elif diasSemana == 'Segunda a Sexta':
                dias.pop()
                for dia in dias:
                    hora = HorarioFuncionamento()
                    hora.dias_da_semana = dia
                    hora.horario_inicio = horaInicio
                    hora.horario_saida = horarioSaida
                    hora.inicio_intervalo = inicioIntervalo
                    hora.final_intervalo = finalIntervalo
                    hora.barbearia = barbearia
                    hora.save()

                return redirect('criar_horario')

            else:
                hora = HorarioFuncionamento()
                hora.dias_da_semana = diasSemana
                hora.horario_inicio = horaInicio
                hora.horario_saida = horarioSaida
                hora.inicio_intervalo = inicioIntervalo
                hora.final_intervalo = finalIntervalo
                hora.barbearia = barbearia
                hora.save()
                return redirect('criar_horario')
        
        messages.warning(request, 'Erro ao cadastrar horario')
        return redirect('criar_horario')



class ProdutosCreate(LoginRequiredMixin, CreateView):
    model = Produtos
    login_url = reverse_lazy('login')
    form_class = ProdutosModelForm
    template_name = 'form_criar/criar_produtos.html'
    success_url = reverse_lazy('produtos')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Produto'
        context['btn'] = 'Cadastrar'
        return context
    

    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia
        produto = Produtos.objects.filter(nome=form.instance.nome)

        if produto:
            messages.error(self.request, 'Produto ja Cadastrado')
            return HttpResponseRedirect(reverse_lazy('produtos'))

        else:  
            messages.success(self.request, 'Produto Cadastrado com Sucesso')     
            serv_form = super().form_valid(form)       
            return serv_form


class EnderecoCreate(LoginRequiredMixin, CreateView):
    model = Endereco
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_endereco.html'
    fields = ['rua', 'numero', 'cep', 'bairro', 'cidade', 'estado']
    success_url = reverse_lazy('dashboard')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Endereço'
        context['btn'] = 'Cadastrar'
        return context
    

    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia       
        serv_form = super().form_valid(form)        
        return serv_form


# update


class BarbeariaUpdate(UpdateView):
    model = Barbearia
    template_name = 'form_editar/form_editar_barbearia.html'
    fields = ['barbearia', 'nome', 'telefone', 'logo']
    success_url = reverse_lazy('dashboard')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Dashboard Barbearia'
        context['btn'] = 'Salvar'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """
        self.object = Barbearia.objects.get(pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class ServicosUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Servicos
    form_class = ServicosModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_servicos.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Servico alterado com Sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Serviço'
        context['btn'] = 'Salvar'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """
        self.object = Servicos.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class ClientesUpdate(LoginRequiredMixin, SuccessMessageMixin ,UpdateView):
    model = Clientes
    form_class = ClienteModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_cliente.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente alterado com Sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        context['btn'] = 'Salvar'
        return context
    

    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Clientes.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class ProfissionaisUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profissionais
    form_class = ProfissionaisModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_profissional.html'
    success_url = reverse_lazy('profissionais')
    success_message = 'Profissional alterado com Sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Profissional'
        context['btn'] = 'Salvar'
        return context
     

    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Profissionais.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class HorarioFuncionamentoUpdate(LoginRequiredMixin, UpdateView):
    model = HorarioFuncionamento
    form_class = HorarioModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_horario.html'
    success_url = reverse_lazy('criar_horario')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horário de Funcionamento'
        context['btn'] = 'Salvar'
        return context 

    
    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """
        self.object = HorarioFuncionamento.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produtos
    form_class = ProdutosModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_produto.html'
    success_url = reverse_lazy('produtos')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Produto'
        context['btn'] = 'Salvar'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Produtos.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class EnderecoUpdate(LoginRequiredMixin, UpdateView):
    model = Endereco
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_endereco.html'
    fields = ['rua', 'numero', 'cep', 'bairro', 'cidade', 'estado']
    success_url = reverse_lazy('dashboard')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Endereço'
        context['btn'] = 'Salvar'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Endereco.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


# delete

class ServicosDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_servico.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Servico deletado com sucesso'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['nome'] = 'Serviço'
        return context

    
    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """
        self.object = Servicos.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object
    

class ClientesDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Clientes
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_cliente.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente deletado com sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Cliente'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Clientes.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class ProfissionalDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Profissionais
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_profissional.html'
    success_url = reverse_lazy('profissionais')
    success_message = 'Profissional deletado com sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Profissional'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Profissionais.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)

        return self.object


class HorarioFuncionamentoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = HorarioFuncionamento
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_horario.html'
    success_url = reverse_lazy('criar_horario')
    success_message = 'Profissional deletado com sucesso'

    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = HorarioFuncionamento.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class EnderecoDelete(LoginRequiredMixin, DeleteView):
    model = Endereco
    login_url = reverse_lazy('login')
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('endereco')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Endereço'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Endereco.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)

        return self.object


class Produtodelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Produtos
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_produto.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto deletado com sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Produto'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Produtos.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)

        return self.object
        