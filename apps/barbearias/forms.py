from pyexpat import model
from django import forms
from stdimage import StdImageField
from .models import Servicos, Clientes, Profissionais, Produtos


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
        

        
class ProfissionaisModalForm(forms.ModelForm):

    class Meta:
        model = Profissionais
        fields = ['nome', 'telefone', 'imagem']
    

    def __init__(self, *args, **kwargs):
        super(ProfissionaisModalForm, self).__init__(*args, **kwargs)
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
        self.fields['imagem'].widget = forms.TextInput(
            attrs={
                'type': 'file', 
                'class': 'form-control'
                })


class ProdutosModalForms(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = ['nome', 'preco', 'descricao', 'imagem']


    def __init__(self, *args, **kwargs):
        super(ProdutosModalForms, self).__init__(*args, **kwargs)
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
        self.fields['imagem'].widget = forms.TextInput(
            attrs={
                'type': 'file',
                'class': 'form-control'
                })

