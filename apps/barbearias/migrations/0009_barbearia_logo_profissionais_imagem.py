# Generated by Django 4.0.4 on 2022-05-16 23:34

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('barbearias', '0008_alter_endereco_barbearia_alter_produtos_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbearia',
            name='logo',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='barbearia/logo'),
        ),
        migrations.AddField(
            model_name='profissionais',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='Profissionais'),
        ),
    ]
