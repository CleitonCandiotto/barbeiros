from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Servicos, Clientes, HorarioFuncionamento, Profissionais, Produtos, Barbearia, Endereco
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ServicosModelForm, ClienteModelForm, ProfissionaisForm


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


# list

class ServicosList(LoginRequiredMixin, ListView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'servicos.html'
    paginate_by = 10


    def get_queryset(self):
        buscaServico = self.request.GET.get('serviço')

        if buscaServico:
            self.object_list = Servicos.objects.filter(
                servico__icontains=buscaServico,
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
    model = Servicos
    form_class = ServicosModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_admin.html'
    success_url = reverse_lazy('servicos')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Serviço'
        context['btn'] = 'Cadastrar'
        return context


    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia
        messages.success(self.request, 'Servico Cadastrado co Sucesso')  
        serv_form = super().form_valid(form)     
        return serv_form


class ClientesCreate(LoginRequiredMixin, CreateView):
    model = Clientes
    form_class = ClienteModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_admin.html'

    success_url = reverse_lazy('clientes')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Cliente'
        context['btn'] = 'Cadastrar'
        return context
    

    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia                    
        serv_form = super().form_valid(form)
        messages.success(self.request, 'Cliente cadastrado com Sucesso')  
                     
        return serv_form


class ProfissionaisCreate(LoginRequiredMixin, CreateView):
    model = Profissionais
    form_class = ProfissionaisForm
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_admin.html'
    success_url = reverse_lazy('profissionais')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Profissional'
        context['btn'] = 'Cadastrar'
        return context
    

    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia   
        serv_form = super().form_valid(form)       
        return serv_form


class HorarioFuncionamentoCreate(LoginRequiredMixin, CreateView):
    model = HorarioFuncionamento
    login_url = reverse_lazy('login')
    template_name = 'horario_atendimento.html'
    fields = ['dias_da_semana', 'horario_inicio', 'horario_saida', 'inicio_intervalo', 'final_intervalo']
    success_url = reverse_lazy('criar_horario')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horário de Funcionamento'
        context['btn'] = 'Cadastrar'
        context['dias'] = HorarioFuncionamento.objects.filter(barbearia=self.request.user.barbearia)
        return context   


    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia
        serv_form = super().form_valid(form)
        return serv_form


class ProdutosCreate(LoginRequiredMixin, CreateView):
    model = Produtos
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_admin.html'
    fields = ['nome', 'preco', 'descricao', 'imagem']
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


class ServicosUpdate(LoginRequiredMixin, UpdateView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_servicos.html'
    fields = ['servicos', 'tempo', 'preco']
    success_url = reverse_lazy('servicos')


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


class ClientesUpdate(LoginRequiredMixin ,UpdateView):
    model = Clientes
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_cliente.html'
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('clientes')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Cliente'
        context['btn'] = 'Salvar'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Clientes.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class ProfissionaisUpdate(LoginRequiredMixin ,UpdateView):
    model = Profissionais
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_profissional.html'
    fields = ['nome', 'telefone', 'imagem']
    success_url = reverse_lazy('profissionais')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Profissional'
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
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_horario.html'
    fields = ['dias_da_semana', 'horario_inicio', 'horario_saida', 'inicio_intervalo', 'final_intervalo']
    success_url = reverse_lazy('criar_horario')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horário de Funcionamento'
        context['btn'] = 'Cadastrar'
        dias = HorarioFuncionamento.objects.filter(barbearia=self.request.user.barbearia)
        context['dias'] = dias         
        return context 

    
    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """
        self.object = HorarioFuncionamento.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produtos
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_produto.html'
    fields = ['nome', 'preco', 'descricao', 'imagem']
    success_url = reverse_lazy('produtos')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Produto'
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
    template_name = 'form_deletar_admin.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Servico deletado com sucesso'


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['nome'] = 'Serviço'
        context['servico'] = Servicos.objects.filter(barbearia=self.request.user.barbearia)
        return context

    
    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """
        self.object = Servicos.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object

    
    def form_valid(self, form):
        success_url = self.get_success_url()
        success_message = self.get_success_message(form.cleaned_data)
        self.object.delete()

        if success_message:
            messages.warning(self.request, success_message)
            
        return HttpResponseRedirect(success_url)


class ClientesDelete(LoginRequiredMixin, DeleteView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('clientes')


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


class ProfissionalDelete(LoginRequiredMixin, DeleteView):
    model = Profissionais
    login_url = reverse_lazy('login')
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('profissionais')


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


class HorarioFuncionamentoDelete(LoginRequiredMixin, DeleteView):
    model = HorarioFuncionamento
    login_url = reverse_lazy('login')
    template_name = 'horario_atendimento.html'
    success_url = reverse_lazy('criar_horario')


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = HorarioFuncionamento.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)
        return self.object

