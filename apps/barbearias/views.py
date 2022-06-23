from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Servicos, Clientes, HorarioFuncionamento, Profissionais, Produtos 
from .models import ContaPagar, Barbearia, Endereco, ContaReceber
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ServicosModelForm, ClienteModelForm,  ProdutosModelForm, ProfissionaisModelForm
from .forms import EnderecoModelForm, BarbeariaModelForm, HorarioModelForm , ContaPagarModelForm
from .forms import ContaReceberModelForm

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


# visualizar

class ContaPagarVisualizar(LoginRequiredMixin, ListView):
    model = ContaPagar
    login_url = reverse_lazy('login')
    template_name = 'visualizar/conta_pagar_view.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conta'] = ContaPagar.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
        return context


class ContaReceberVisualizar(LoginRequiredMixin, ListView):
    model = ContaReceber
    login_url = reverse_lazy('login')
    template_name = 'visualizar/conta_receber_view.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conta'] = ContaReceber.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
        return context


# list

class ServicosList(LoginRequiredMixin, ListView):
    model = Servicos
    login_url = reverse_lazy('login')
    template_name = 'list/servicos.html'
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
    template_name = 'list/clientes.html'
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
    template_name = 'list/profissionais.html'


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
    template_name = 'list/produtos.html'


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
    template_name = 'list/endereco.html'


    def get_queryset(self):
        self.object_list = Endereco.objects.filter(
            barbearia=self.request.user.barbearia
            )
        return self.object_list
    

class ContaPagarList(LoginRequiredMixin, ListView):
    model = ContaPagar
    login_url = reverse_lazy('login')
    template_name = 'list/conta_pagar.html'


    def get_queryset(self):
        buscaConta = self.request.GET.get('pg')

        if buscaConta:
            self.object_list = ContaPagar.objects.filter(
                conta__icontains=buscaConta,
                barbearia=self.request.user.barbearia
                )
       
        else:
            self.object_list = ContaPagar.objects.filter(
                barbearia=self.request.user.barbearia
                )

        return self.object_list
    

class ContaReceberList(LoginRequiredMixin, ListView):
    model = ContaReceber
    login_url = reverse_lazy('login')
    template_name = 'list/conta_receber.html'


    def get_queryset(self):
        buscaConta = self.request.GET.get('pg')

        if buscaConta:
            self.object_list = ContaReceber.objects.filter(
                conta__icontains=buscaConta,
                barbearia=self.request.user.barbearia
                )
       
        else:
            self.object_list = ContaReceber.objects.filter(
                barbearia=self.request.user.barbearia
                )

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
    template_name = 'form_criar/horario_atendimento.html'
    success_url = reverse_lazy('criar_horario')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horário de Funcionamento'
        context['btn'] = 'Cadastrar'
        context['dias'] = HorarioFuncionamento.objects.filter(
            barbearia=self.request.user.barbearia
            )
        return context   


    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        barbearia = self.request.user.barbearia
        diasSemana = self.request.POST.get('dias_da_semana')
        horaInicio = self.request.POST.get('horario_inicio')
        horaSaida = self.request.POST.get('horario_saida')
        inicioIntervalo = self.request.POST.get('inicio_intervalo')
        finalIntervalo = self.request.POST.get('final_intervalo')
        dias = [
            'Segunda-feira', 
            'Terça-feira', 
            'Quarta-feira', 
            'Quinta-feira', 
            'Sexta-feira', 
            'Sábado'
            ]

        valida = self.valida_hora(horaInicio, horaSaida, inicioIntervalo, finalIntervalo)

        if valida:               
            if form.is_valid():
                if diasSemana == 'Segunda a Sábado': 
                    for dia in dias:
                        hora = HorarioFuncionamento()
                        hora.dias_da_semana = dia
                        hora.horario_inicio = horaInicio
                        hora.horario_saida = horaSaida
                        hora.inicio_intervalo = inicioIntervalo
                        hora.final_intervalo = finalIntervalo
                        hora.barbearia = barbearia
                        hora.save()
                    messages.success(request, 'Horario criado com sucesso')
                    return redirect('criar_horario')

                elif diasSemana == 'Segunda a Sexta':
                    dias.pop()
                    for dia in dias:
                        hora = HorarioFuncionamento()
                        hora.dias_da_semana = dia
                        hora.horario_inicio = horaInicio
                        hora.horario_saida = horaSaida
                        hora.inicio_intervalo = inicioIntervalo
                        hora.final_intervalo = finalIntervalo
                        hora.barbearia = barbearia
                        hora.save()
                    messages.success(request, 'Horario criado com sucesso')
                    return redirect('criar_horario')

                else:
                    hora = HorarioFuncionamento()
                    hora.dias_da_semana = diasSemana
                    hora.horario_inicio = horaInicio
                    hora.horario_saida = horaSaida
                    hora.inicio_intervalo = inicioIntervalo
                    hora.final_intervalo = finalIntervalo
                    hora.barbearia = barbearia
                    hora.save()
                    messages.success(request, 'Horario criado com sucesso')
                    return redirect('criar_horario')
        
        messages.warning(request, 'Erro ao cadastrar horario')
        return redirect('criar_horario')


    def valida_hora(self, hI:str, hS:str, iI:str=None, fI:str=None):
        hInicio = self.convert_srt(hI)
        hSaida = self.convert_srt(hS)
        iIntervalo = self.convert_srt(iI)
        fIntervalo = self.convert_srt(fI)

        if hInicio < hSaida and iIntervalo <= fIntervalo:
            return True    
        return False


    def convert_srt(self, valor:str):
        if valor:
            valor = valor.split(':')
            valor = int(''.join(valor))
            return valor
        return 0


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
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        produto = self.request.POST.get('nome')
        produtoDb = Produtos.objects.filter(nome=produto)

        if not produtoDb:
            if form.is_valid():
                form.instance.barbearia = self.request.user.barbearia
                messages.success(request, f'Produto: {produto} cadastrado com sucesso')
                form.save()
                return redirect('produtos')
     
        messages.warning(request, 'Produto ja cadastrado')
        return redirect('produtos')


class EnderecoCreate(LoginRequiredMixin, CreateView):
    model = Endereco
    form_class = EnderecoModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_criar/criar_endereco.html'
    success_url = reverse_lazy('perfil')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Endereço'
        context['btn'] = 'Cadastrar'
        return context
    

    def form_valid(self, form):
        form.instance.barbearia = self.request.user.barbearia       
        serv_form = super().form_valid(form)        
        return serv_form


class ContaPagarCreate(LoginRequiredMixin, CreateView):
    model = ContaPagar
    form_class = ContaPagarModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_criar/criar_contas_pagar.html'
    success_url = reverse_lazy('conta_pagar')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Conta'
        context['btn'] = 'Cadastrar'
        return context

    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        pago = self.request.POST.get('pago')

        conta = lambda pago: 'Pago' if pago else 'A Pagar'

        if form.is_valid():
            form.instance.barbearia = self.request.user.barbearia
            form.instance.infoPago = conta(pago)
            messages.success(request, 'Conta cadastrada com Sucesso')
            form.save()
            return redirect('conta_pagar')

        else:
            messages.warning(request, 'Erro ao cadastrar conta')
            return redirect('conta_pagar')


class ContaReceberCreate(LoginRequiredMixin, CreateView):
    model = ContaReceber
    form_class = ContaReceberModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_criar/criar_contas_receber.html'
    success_url = reverse_lazy('conta_receber')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Conta'
        context['btn'] = 'Cadastrar'
        return context

    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        pago = self.request.POST.get('pago')

        conta = lambda pago: 'Recebido' if pago else 'A Receber'

        if form.is_valid():
            form.instance.barbearia = self.request.user.barbearia
            form.instance.infoPago = conta(pago)
            messages.success(request, 'Conta cadastrada com Sucesso')
            form.save()
            return redirect('conta_receber')

        else:
            messages.warning(request, 'Erro ao cadastrar conta')
            return redirect('conta_receber')

# update

class BarbeariaUpdate(UpdateView):
    model = Barbearia
    form_class = BarbeariaModelForm
    template_name = 'form_editar/form_editar_barbearia.html'
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
        self.object = Barbearia.objects.get(
            pk=self.kwargs['pk'], 
            usuario=self.request.user
            )
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
        self.object = Servicos.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
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
        self.object = Clientes.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
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
        self.object = Profissionais.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
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
        self.object = HorarioFuncionamento.objects.get(
            pk=self.kwargs['pk'],
            barbearia=self.request.user.barbearia
            )
        return self.object


    def post(self, request, *args, **kwargs) :

        hora = HorarioFuncionamento.objects.get(id=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=hora)
        barbearia = self.request.user.barbearia
        diasSemana = self.request.POST.get('dias_da_semana')
        horaInicio = self.request.POST.get('horario_inicio')
        horarioSaida = self.request.POST.get('horario_saida')
        inicioIntervalo = self.request.POST.get('inicio_intervalo')
        finalIntervalo = self.request.POST.get('final_intervalo')

        if form.is_valid():
            hora.dias_da_semana = diasSemana
            hora.horario_inicio = horaInicio
            hora.horario_saida = horarioSaida
            hora.inicio_intervalo = inicioIntervalo
            hora.final_intervalo = finalIntervalo
            hora.barbearia = barbearia
            hora.save()
            messages.success(request, 'Horario editado com sucesso')
            return redirect('criar_horario')

        messages.warning(request, 'Erro ao editar horario ')
        return redirect('criar_horario')


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
        self.object = Produtos.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
        return self.object


class EnderecoUpdate(LoginRequiredMixin, UpdateView):
    model = Endereco
    form_class = EnderecoModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_endereco.html'
    success_url = reverse_lazy('perfil')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Endereço'
        context['btn'] = 'Salvar'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Endereco.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
        return self.object


class ContaPagarUpdate(LoginRequiredMixin, UpdateView):
    model = ContaPagar
    form_class = ContaPagarModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_conta_pagar.html'
    success_url = reverse_lazy('conta_pagar')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Conta'
        context['btn'] = 'Salvar'
        return context
    

    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = ContaPagar.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
        return self.object


    def post(self, request, *args, **kwargs):
        contaPagar = ContaPagar.objects.get(id=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=contaPagar)
        pago = self.request.POST.get('pago')

        conta = lambda pago: 'Pago' if pago else 'A Pagar'

        if form.is_valid():
            form.instance.barbearia = self.request.user.barbearia
            form.instance.infoPago = conta(pago)
            messages.success(request, 'Conta Editada com Sucesso')
            form.save()
            return redirect('conta_pagar')

        else:
            messages.warning(request, 'Erro ao editar conta')
            return redirect('conta_pagar')


class ContaReceberUpdate(LoginRequiredMixin, UpdateView):
    model = ContaReceber
    form_class = ContaReceberModelForm
    login_url = reverse_lazy('login')
    template_name = 'form_editar/form_editar_conta_receber.html'
    success_url = reverse_lazy('conta_receber')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Conta'
        context['btn'] = 'Salvar'
        return context
    

    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = ContaReceber.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
        return self.object


    def post(self, request, *args, **kwargs):
        contaReceber = ContaReceber.objects.get(id=self.kwargs['pk'])
        form = self.form_class(request.POST, instance=contaReceber)
        pago = self.request.POST.get('pago')

        conta = lambda pago: 'Recebido' if pago else 'A Receber'

        if form.is_valid():
            form.instance.barbearia = self.request.user.barbearia
            form.instance.infoPago = conta(pago)
            messages.success(request, 'Conta Editada com Sucesso')
            form.save()
            return redirect('conta_receber')

        else:
            messages.warning(request, 'Erro ao editar conta')
            return redirect('conta_receber')

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
        self.object = Servicos.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
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
        self.object = Clientes.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
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
        self.object = Profissionais.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )

        return self.object


class HorarioFuncionamentoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = HorarioFuncionamento
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_horario.html'
    success_url = reverse_lazy('criar_horario')
    success_message = 'Horario deletado com sucesso'

    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = HorarioFuncionamento.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )
        return self.object


class EnderecoDelete(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Endereco
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_endereco.html'
    success_url = reverse_lazy('perfil')
    success_message = 'Endereço deletado com sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Endereço'
        return context


    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = Endereco.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )

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
        self.object = Produtos.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )

        return self.object


class ContaPagarDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ContaPagar
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_conta_pagar.html'
    success_url = reverse_lazy('conta_pagar')
    success_message = 'Conta deletada com sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Conta'
        return context

    
    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = ContaPagar.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )

        return self.object


class ContaReceberDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ContaReceber
    login_url = reverse_lazy('login')
    template_name = 'form_excluir/form_excluir_conta_receber.html'
    success_url = reverse_lazy('conta_receber')
    success_message = 'Conta deletada com sucesso'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Conta'
        return context

    
    def get_object(self, queryset=None):
        """
        Func para somente o usuario conseguir alterar os dados dele
        """        
        self.object = ContaReceber.objects.get(
            pk=self.kwargs['pk'], 
            barbearia=self.request.user.barbearia
            )

        return self.object
