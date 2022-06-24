# Generated by Django 4.0.4 on 2022-06-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0019_alter_horariofuncionamento_final_intervalo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='final_intervalo',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Final Intervalo'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='horario_inicio',
            field=models.CharField(max_length=5, verbose_name='Horário Início'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='horario_saida',
            field=models.CharField(max_length=5, verbose_name='Horário Saída'),
        ),
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='inicio_intervalo',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Início Intervalo'),
        ),
    ]