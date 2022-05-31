from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.barbearias import forms
from .models import CustomUser
from django import forms



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password1' ,'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class LoginFormAuthentication(forms.Form):
    username = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"E-mail"}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(),
    )


    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        usuario_db = CustomUser.objects.filter(email=username)

        if not usuario_db:
            raise forms.ValidationError('E-mail não cadastrado')