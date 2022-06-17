# Generated by Django 4.0.4 on 2022-06-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0014_alter_horariofuncionamento_dias_da_semana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='final_intervalo',
            field=models.CharField(blank=True, help_text='Ex "00:00"', max_length=5, null=True, verbose_name='Final Intervalo'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='horario_inicio',
            field=models.CharField(help_text='Ex "00:00"', max_length=5, verbose_name='Horário Início'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='horario_saida',
            field=models.CharField(help_text='Ex "00:00"', max_length=5, verbose_name='Horário Saída'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='inicio_intervalo',
            field=models.CharField(blank=True, help_text='Ex "00:00"', max_length=5, null=True, verbose_name='Início Intervalo'),
        ),
        migrations.AlterField(
            model_name='profissionais',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='Profissionais'),
        ),
    ]
