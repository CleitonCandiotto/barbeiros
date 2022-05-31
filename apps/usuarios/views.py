from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from apps.usuarios.models import CustomUser

from .forms import CustomUserCreationForm, LoginFormAuthentication
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


def login_user(request):

    if request.method =='POST':
        form = LoginFormAuthentication(request.POST or None)
        email = form.instance.email
        password = request.POST['password']
        user_db = CustomUser.objects.filter(email=email).first()

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')       

        else:       
            messages.error(request, 'Este Campo é Obrigatório')
            return redirect('login')
    else:
        return render(request, 'login.html', {'form':form})



from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        Barbearia.objects.create(barbearia=' ', usuario=user)

        # You must return the original result.
        return user