from django import forms
from stdimage import StdImageField
from .models import Servicos, Clientes, Profissionais
from django.contrib.auth.forms import AuthenticationForm

class ServicosModelForm(forms.ModelForm):
 
    class Meta:
        model = Servicos
        fields = ['servicos', 'tempo', 'preco']
        

    def clean(self):
        servicos = self.cleaned_data.get('servicos')

        servico_db = Servicos.objects.filter(servicos=servicos)

        if servico_db:
            raise forms.ValidationError('Servico Já cadastrado')

       
class ClienteModelForm(forms.ModelForm):
 
    class Meta:
        model = Clientes
        fields = ['nome', 'telefone']
        

    def clean(self):
        nome = self.cleaned_data.get('nome')
        telefone = self.cleaned_data.get('telefone')

        cliente_db = Clientes.objects.filter(nome=nome)
        telefone_db = Clientes.objects.filter(telefone=telefone)

        if cliente_db and telefone_db:
            raise forms.ValidationError('Cliente já Cadastrado')
        
        if len(telefone_db) > 13:
            raise forms.ValidationError('Entre com um telefone valido')


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
