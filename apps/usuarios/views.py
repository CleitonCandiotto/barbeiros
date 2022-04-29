from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm



class UsuarioCreate(CreateView):
    template_name = 'form_cadastro.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro '
        context['btn'] = 'Cadastar'

        return context



    


   