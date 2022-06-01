from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views 
from .views import UsuarioCreate
from allauth.account.views import PasswordChangeView


urlpatterns = [
    path('criar-usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
    path('accounts/password/change/',PasswordChangeView.as_view(
        success_url = reverse_lazy('dashboard')
    ), 
    name='account_password_change')
    
]