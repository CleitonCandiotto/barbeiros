from django.db import models
from stdimage import StdImageField
from apps.usuarios.models import CustomUser



class Barbearia(models.Model):
    barbearia = models.CharField(max_length=200, verbose_name='Barbearia')
    nome = models.CharField(max_length=200, verbose_name='Nome', help_text='Informe aqui seu nome completo.')
    telefone = models.CharField(max_length=16, verbose_name='Telefone')
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


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
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
    

    def __srt__(self):
        return f'Endereço {self.barbearia.barbearia}'


class Profissionais(models.Model):
    nome = models.CharField(blank=True, null=True, max_length=100, verbose_name='Nome')
    telefone = models.CharField(blank=True, null=True,max_length=16, verbose_name='Telefone')
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Profissional'
        verbose_name_plural = 'Profissionais'

    
    def __str__(self):
        return f'{self.nome} - {self.barbearia.barbearia}'


class Servicos(models.Model):
    TEMPO_CHOICE = (
        ('15', '15 Minutos'),
        ('30', '30 Minutos'),
        ('01', '01 Hora'),
    )
    servicos = models.CharField(max_length=100, help_text='Ex: Barba - Cabelo - Bigode', 
                                verbose_name='Nome do Serviço')
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
        ('Todos os dias','Todos os dias'), ('Segunda a Sexta','Segunda a Sexta'),( 'Segunda a Sábado', 'Segunda a Sábado'),
        ('Segunda Feira','Segunda Feira'), ('Terça Feira','Terça Feira'), ('Quarta Feira', 'Quarta Freira'),
        ('Quinta Feira','Quinta Feira'), ('Sexta Feira','Sexta Feira'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo'),
    )

    dias_da_semana = models.CharField(max_length=16, choices=DIAS_CHOICE)
    horario_inicio = models.TimeField(verbose_name='Horário Início', help_text='Ex "00:00"')
    horario_saida = models.TimeField(verbose_name='Horário Saída', help_text='Ex "00:00"')
    inicio_intervalo = models.TimeField(verbose_name='Início Intervalo', help_text='Ex "00:00"')
    final_intervalo = models.TimeField(verbose_name='Final Intervalo', help_text='Ex "00:00"')
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT)


    class Meta:
        verbose_name = 'Horário de Atendimento'
        verbose_name_plural = 'Horários de Atendimento'

    
    def __str__(self):
        return f'Horário Atendimento - {self.barbearia.barbearia}'


class AgendaHorario(models.Model):
    pass
    


