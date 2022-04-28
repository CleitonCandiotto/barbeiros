from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserCreationForm



class UsuarioCreate(CreateView):
    template_name = 'form_cadastro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    


   