# Generated by Django 4.0.4 on 2022-05-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0011_alter_servicos_servicos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicos',
            name='servicos',
            field=models.CharField(default=1, help_text='Ex: Barba - Cabelo - Bigode', max_length=100, verbose_name='Serviço'),
            preserve_default=False,
        ),
    ]
