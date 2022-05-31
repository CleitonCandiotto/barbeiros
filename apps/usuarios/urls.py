from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import UsuarioCreate, login_user


urlpatterns = [
    path('criar-usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('login/', login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
    
]