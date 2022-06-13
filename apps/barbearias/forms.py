from django import forms
from stdimage import StdImageField
from .models import Servicos, Clientes, Profissionais


class ServicosModelForm(forms.ModelForm):


    class Meta:
        model = Servicos
        fields = ['servicos', 'tempo', 'preco']


    def __init__(self, *args, **kwargs):
        super(ServicosModelForm, self).__init__(*args, **kwargs)
        self.fields['servicos'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['tempo'].widget.attrs['class'] = 'form-control'
        self.fields['preco'].widget = forms.TextInput(attrs={'type': 'number', 'class': 'form-control'})



class ClienteModelForm(forms.ModelForm):
 
    class Meta:
        model = Clientes
        fields = ['nome', 'telefone']
        



class ProfissionaisForm(forms.ModelForm):

    imagem = StdImageField(upload_to='Profissionais', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True},
        'thumb': {"width": 30, "height": 30, "crop": True},
    }, null=True, blank=True)


    class Meta:
        model = Profissionais
        fields = ['nome', 'telefone', 'imagem']
    

    def clean(self):
        nome = self.cleaned_data.get('nome')
        telefone = self.cleaned_data.get('telefone')

        profissional_db = Profissionais.objects.filter(nome=nome)
        telefone_db = Profissionais.objects.filter(telefone=telefone)

        if profissional_db and telefone_db:
            raise forms.ValidationError('Cliente já Cadastrado')

        if len(telefone_db) > 13:
            raise forms.ValidationError('Entre com um telefone valido')
