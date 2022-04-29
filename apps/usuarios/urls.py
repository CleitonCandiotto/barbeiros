from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import UsuarioCreate
from .forms import CustomUserCreationForm

urlpatterns = [
    path('criar-usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('login/', auth_views.LoginView.as_view(
        template_name = 'login.html',
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
    
]