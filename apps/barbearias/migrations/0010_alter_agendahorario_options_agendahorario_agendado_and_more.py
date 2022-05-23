# Generated by Django 4.0.4 on 2022-05-23 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0009_barbearia_logo_profissionais_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendahorario',
            options={'verbose_name': 'Agenda Horario', 'verbose_name_plural': 'Agenda Horarios'},
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='agendado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='antendido',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='barbearia',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='barbearias.barbearia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='barbearias.clientes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='data',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='horario',
            field=models.CharField(default=None, help_text='Ex "00:00"', max_length=5, verbose_name='Hora'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='profissional',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='barbearias.profissionais'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agendahorario',
            name='servico',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='barbearias.servicos'),
            preserve_default=False,
        ),
    ]
