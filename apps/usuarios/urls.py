from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UsuarioCreate
from .forms import CustomUserCreationForm

urlpatterns = [
    path('criar-usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('login/', LoginView.as_view(
        template_name = 'login.html',
        ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout' ),
]