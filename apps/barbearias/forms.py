from django import forms
from .models import Servicos, Clientes, Profissionais, Produtos, HorarioFuncionamento


class ServicosModelForm(forms.ModelForm):

    class Meta:
        model = Servicos
        fields = ['servicos', 'tempo', 'preco']


    def __init__(self, *args, **kwargs):
        super(ServicosModelForm, self).__init__(*args, **kwargs)
        self.fields['servicos'].widget = forms.TextInput(
            attrs={
                'class': 'form-control'
                })
        self.fields['tempo'].widget.attrs['class'] = 'form-control'
        self.fields['preco'].widget = forms.TextInput(
            attrs={
                'type': 'number', 
                'class': 'form-control'
                })


class ClienteModelForm(forms.ModelForm):
 
    class Meta:
        model = Clientes
        fields = ['nome', 'telefone']

    
    def __init__(self, *args, **kwargs):
        super(ClienteModelForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Nome Completo'
            })
        self.fields['telefone'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '(xx)00000-0000'
                })
        

        
class ProfissionaisModelForm(forms.ModelForm):

    class Meta:
        model = Profissionais
        fields = ['nome', 'telefone', 'imagem']
    

    def __init__(self, *args, **kwargs):
        super(ProfissionaisModelForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Nome Completo'
            })
        self.fields['telefone'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '(xx)00000-0000'
                })
        

class ProdutosModelForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'descricao', 'imagem']


    def __init__(self, *args, **kwargs):
        super(ProdutosModelForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            'placeholder': 'Nome Completo'
            })
        self.fields['preco'].widget = forms.TextInput(
            attrs={
                'type': 'number', 
                'class': 'form-control'
                })
        self.fields['descricao'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'rows': '10'
                })


class HorarioModelForm(forms.ModelForm):
    
    class Meta:
        model = HorarioFuncionamento
        fields = ['dias_da_semana', 'horario_inicio', 'horario_saida', 'inicio_intervalo', 'final_intervalo']

    
    def __init__(self, *args, **kwargs):
        super(HorarioModelForm, self).__init__(*args, **kwargs)
        self.fields['dias_da_semana'].widget.attrs['class'] = 'form-control'
        self.fields['horario_inicio'].widget = forms.TextInput(
            attrs={
            'type': 'time',
            'class': 'form-control',
            })
        self.fields['horario_saida'].widget = forms.TextInput(
            attrs={
            'type': 'time',
            'class': 'form-control',
            })
        self.fields['inicio_intervalo'].widget = forms.TextInput(
            attrs={
            'type': 'time',
            'class': 'form-control',
            })
        self.fields['final_intervalo'].widget = forms.TextInput(
            attrs={
            'type': 'time',
            'class': 'form-control',
            })
