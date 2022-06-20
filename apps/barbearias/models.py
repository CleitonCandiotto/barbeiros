from xml.etree.ElementInclude import default_loader
from django.db import models
from stdimage import StdImageField
from apps.usuarios.models import CustomUser



class Barbearia(models.Model):
    barbearia = models.CharField(max_length=200, verbose_name='Barbearia')
    nome = models.CharField(max_length=200, verbose_name='Nome', help_text='Informe aqui seu nome completo.')
    telefone = models.CharField(max_length=16, verbose_name='Telefone')
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    logo = StdImageField(upload_to='barbearia/logo', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True},
        'thumb': {"width": 30, "height": 30, "crop": True},
    }, null=True, blank=True)



    class Meta:
        verbose_name = 'Barbearia'
        verbose_name_plural = 'Barbearias'


    def __str__(self):
        return self.barbearia


class Endereco(models.Model):
    ESTADO_CHOICE=(
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    rua = models.CharField(max_length=150, verbose_name='Rua')
    numero = models.CharField(max_length=5, verbose_name='N°')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=200, verbose_name='Cidade')
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICE, verbose_name='UF')
    barbearia = models.OneToOneField(Barbearia, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
    

    def __str__(self):
        return f'Endereço {self.barbearia}'


class Profissionais(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    telefone = models.CharField(max_length=16, verbose_name='Telefone')
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)
    imagem = StdImageField(upload_to='profissionais', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True},
        'thumb': {"width": 30, "height": 30, "crop": True},
    }, null=True, blank=True)


    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    
    def __str__(self):
        return f'{self.nome}'


class Servicos(models.Model):
    TEMPO_CHOICE = (
        ('15', '15 Minutos'),
        ('30', '30 Minutos'),
        ('01', '01 Hora'),
    )
    servicos = models.CharField(max_length=100, help_text='Ex: Barba - Cabelo - Bigode', 
                                verbose_name='Serviço',)
    tempo = models.CharField(max_length=2, choices=TEMPO_CHOICE)
    preco = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Preço(R$)')
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    
    def __str__(self):
        return self.servicos



class HorarioFuncionamento(models.Model):

    DIAS_CHOICE = (
        ('Segunda a Sexta','Segunda a Sexta'),
        ( 'Segunda a Sábado', 'Segunda a Sábado'),
        ('Segunda-feira','Segunda-feira'), 
        ('Terça-feira','Terça-feira'), 
        ('Quarta-feira', 'Quarta-freira'),
        ('Quinta-feira','Quinta-feira'), 
        ('Sexta-feira','Sexta-feira'), 
        ('Sábado', 'Sábado'), 
        ('Domingo', 'Domingo'),
    )

    dias_da_semana = models.CharField(max_length=16, choices=DIAS_CHOICE)
    horario_inicio = models.CharField(max_length=5 ,verbose_name='Horário Início')
    horario_saida = models.CharField(max_length=5 ,verbose_name='Horário Saída')
    inicio_intervalo = models.CharField(max_length=5 ,verbose_name='Início Intervalo', blank=True, null=True)
    final_intervalo = models.CharField(max_length=5 ,verbose_name='Final Intervalo', blank=True, null=True )
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Horário de Atendimento'
        verbose_name_plural = 'Horários de Atendimento'

    
    def __str__(self):
        return f'Horário Atendimento - {self.barbearia.barbearia}'


class Clientes(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome')
    telefone = models.CharField(max_length=16, verbose_name='Telefone')
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    
    def __str__(self):
        return self.nome
    

class Produtos(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    preco = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')
    descricao = models.TextField(max_length=250, verbose_name='Descrição', null=True, blank=True)
    imagem = StdImageField(upload_to='produtos', variations={
        'thumbnail': {"width": 100, "height": 100, "crop": True},
        'thumb': {"width": 30, "height": 30, "crop": True},
    }, null=True, blank=True)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)
   


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    
    def __str__(self):
        return self.nome


class AgendaHorario(models.Model):
    barbearia = models.ForeignKey(Barbearia, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissionais, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    data = models.CharField(max_length=10)
    horario = models.CharField(max_length=5 ,verbose_name='Hora', help_text='Ex "00:00"')
    agendado = models.BooleanField(default=False)
    antendido = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Agenda Horario'
        verbose_name_plural = 'Agenda Horarios'

    
    def __str__(self):
        return f'Agenda Horário Cliente:{self.cliente.nome}'
