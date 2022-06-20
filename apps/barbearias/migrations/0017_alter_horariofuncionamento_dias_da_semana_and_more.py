# Generated by Django 4.0.4 on 2022-06-20 12:14

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0016_alter_produtos_preco_alter_profissionais_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='dias_da_semana',
            field=models.CharField(choices=[('Segunda a Sexta', 'Segunda a Sexta'), ('Segunda a Sábado', 'Segunda a Sábado'), ('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-freira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=16),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='final_intervalo',
            field=models.TimeField(blank=True, null=True, verbose_name='Final Intervalo'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='horario_inicio',
            field=models.TimeField(verbose_name='Horário Início'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='horario_saida',
            field=models.TimeField(verbose_name='Horário Saída'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='inicio_intervalo',
            field=models.TimeField(blank=True, null=True, verbose_name='Início Intervalo'),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='profissionais',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='profissionais'),
        ),
    ]
