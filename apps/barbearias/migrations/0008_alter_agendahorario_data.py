# Generated by Django 4.0.4 on 2022-08-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0007_alter_agendahorario_horariofim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendahorario',
            name='data',
            field=models.DateField(default=False),
        ),
    ]
