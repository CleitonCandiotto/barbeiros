from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import LoginForm, SignupForm

from .models import CustomUser
from apps.barbearias.models import Barbearia
from django import forms



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password1' ,'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})


class UserSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})  
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})   


    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(UserSignupForm, self).save(request)

        Barbearia.objects.create(barbearia=' ', usuario=user)

        # You must return the original result.
        return user    
