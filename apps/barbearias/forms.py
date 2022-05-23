from django import forms

from .models import Servicos


class ServicosModelForm(forms.Form):
    class Meta:
        model = Servicos
        fields = ['servicos', 'tempo', 'preco']

    
    def clean(self):
        servicos = self.cleaned_data('servicos')
        servicos_db = Servicos.objects.filter(servicos=servicos)

        if servicos_db:
            raise ValueError('Serviço já cadastrado')
        
        return servicos
