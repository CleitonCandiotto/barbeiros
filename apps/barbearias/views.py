from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Servicos, Clientes, HorarioFuncionamento
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(TemplateView):
    template_name = 'dashboard.html'


# list

class ServicosList(LoginRequiredMixin, ListView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'servicos.html'


    def get_queryset(self):
        self.object_list = Servicos.objects.filter(barbearia=self.request.user.barbearia)
        return self.object_list


class ClientesList(LoginRequiredMixin, ListView):
    model = Clientes
    login_url = reverse_lazy('login')
    template_name = 'clientes.html'


    def get_queryset(self):
        self.object_list = Clientes.objects.filter(barbearia=self.request.user.barbearia)
        return self.object_list

# create

class ServicosCreate(LoginRequiredMixin, CreateView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_admin.html'
    fields = ['servicos', 'tempo', 'preco']
    success_url = reverse_lazy('servicos')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastrar Serviço'
        context['btn'] = 'Cadastrar'

        return context

    
    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia
        
        serv_form = super().form_valid(form)
        
        return serv_form



class ClientesCreate(LoginRequiredMixin, CreateView):
    model = Clientes
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_admin.html'
    fields = ['nome', 'telefone']
    success_url = reverse_lazy('clientes')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastrar Cliente'
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
    success_url = reverse_lazy('dashboard')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Horário de Funcionamento'
        context['btn'] = 'Cadastrar'

        context['horario'] = HorarioFuncionamento.objects.filter(barbearia=self.request.user.barbearia)

        return context   



    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia
        
        serv_form = super().form_valid(form)
        
        return serv_form

# update

class ServicosUpdate(LoginRequiredMixin, UpdateView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'form_cadastro_admin.html'
    fields = ['servicos', 'tempo', 'preco']
    success_url = reverse_lazy('servicos')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastrar Serviço'
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
    template_name = 'form_cadastro_admin.html'
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


class HorarioFuncionamentoUpdate(LoginRequiredMixin, UpdateView):
    model = HorarioFuncionamento
    login_url = reverse_lazy('login')
    template_name = 'horario_atendimento.html'
    fields = ['dias_da_semana', 'horario_inicio', 'horario_saida', 'inicio_intervalo', 'final_intervalo']
    success_url = reverse_lazy('criar_horario')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Horário de Funcionamento'
        context['btn'] = 'Cadastrar'

        context['horario'] = HorarioFuncionamento.objects.filter(barbearia=self.request.user.barbearia)

        return context 

    
    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """
        self.object = HorarioFuncionamento.objects.get(pk=self.kwargs['pk'], barbearia=self.request.user.barbearia)

        return self.object


# delete

class ServicosDelete(LoginRequiredMixin, DeleteView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'form_excluir.html'
    success_url = reverse_lazy('servicos')


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
