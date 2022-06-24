from django import forms
from .models import Barbearia, ContaReceber, Endereco, Servicos, Clientes, Profissionais, Produtos, HorarioFuncionamento
from .models import ContaPagar


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
                'step': '0.01',
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
                'step': '0.01',
                'class': 'form-control'
                })
        self.fields['descricao'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
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


class EnderecoModelForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'cep', 'bairro', 'cidade', 'estado']


    def __init__(self, *args, **kwargs):
        super(EnderecoModelForm, self).__init__(*args, **kwargs)
        self.fields['rua'].widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            })
        self.fields['numero'].widget = forms.TextInput(
            attrs={
                'class': 'form-control'
                })
        self.fields['cep'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                })
        self.fields['bairro'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                })
        self.fields['cidade'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                })
        self.fields['estado'].widget.attrs['class'] = 'form-control'


class BarbeariaModelForm(forms.ModelForm):

    class Meta:
        model = Barbearia
        fields = ['barbearia', 'nome', 'telefone', 'logo']


    def __init__(self, *args, **kwargs):
        super(BarbeariaModelForm, self).__init__(*args, **kwargs)
        self.fields['barbearia'].widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            })
        self.fields['nome'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome Completo'
                })
        self.fields['telefone'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                })


class ContaPagarModelForm(forms.ModelForm):

    class Meta:
        model = ContaPagar
        fields = ['conta', 'valor', 'dataVencimento','pago']


    def __init__(self, *args, **kwargs):
        super(ContaPagarModelForm, self).__init__(*args, **kwargs)
        self.fields['conta'].widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            })
        self.fields['valor'].widget = forms.TextInput(
            attrs={
                'type': 'number',
                'step': '0.01',
                'class': 'form-control',
                })
        self.fields['dataVencimento'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : 'date',
                })
        self.fields['pago'].widget = forms.CheckboxInput(
            attrs={
                'class':'form-check-label',
            })


class ContaReceberModelForm(forms.ModelForm):

    class Meta:
        model = ContaReceber
        fields = ['conta', 'valor', 'dataVencimento','pago']


    def __init__(self, *args, **kwargs):
        super(ContaReceberModelForm, self).__init__(*args, **kwargs)
        self.fields['conta'].widget = forms.TextInput(
            attrs={
            'class': 'form-control',
            })
        self.fields['valor'].widget = forms.TextInput(
            attrs={
                'type': 'number',
                'step': '0.01',
                'class': 'form-control',
                })
        self.fields['dataVencimento'].widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'type' : 'date',
                })
        self.fields['pago'].widget = forms.CheckboxInput(
            attrs={
                'class':'form-check-label',
            })
