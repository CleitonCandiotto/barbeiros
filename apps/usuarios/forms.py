from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.conf import settings
from django.contrib.auth import get_user_model



class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = CustomUser
        fields = ('email', 'password1' ,'password2')


class CustomUserChangeForm(UserChangeForm):


    class Meta:
        model = CustomUser
        fields = ('email',)
