from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import UsuarioCreate


urlpatterns = [
    path('criar-usuario/', UsuarioCreate.as_view(), name='criar_usuario'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
    
]