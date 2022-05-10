from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from apps.usuarios.models import CustomUser
from .forms import CustomUserCreationForm
from apps.barbearias.models import Barbearia
from django.contrib.auth import authenticate, login



class UsuarioCreate(CreateView):
    template_name = 'form_cadastro.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro '
        context['btn'] = 'Cadastar'

        return context
    

    def form_valid(self, form):
        form_cadastro = super().form_valid(form)

        Barbearia.objects.create(barbearia=' ', usuario=self.object)

        email = form.cleaned_data['email']
        password = form.cleaned_data['password1']

        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return form_cadastro

        return form_cadastro

