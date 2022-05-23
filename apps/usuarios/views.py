from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import CustomUserCreationForm
from apps.barbearias.models import Barbearia
from django.contrib.auth import authenticate, login


class UsuarioCreate(SuccessMessageMixin, CreateView):
    template_name = 'form_cadastro.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('dashboard')
    success_message = 'Usuario criado com sucesso'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro '
        context['btn'] = 'Cadastar'

        return context
    

    def form_valid(self, form):
        form_cadastro = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)

        if success_message:
            messages.success(self.request, success_message)

        Barbearia.objects.create(barbearia=' ', usuario=self.object)

        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']

        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return form_cadastro

        return form_cadastro
    

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data


class Login(views.LoginView):
    template_name = 'login.html'


    def clean(request):
        pass
