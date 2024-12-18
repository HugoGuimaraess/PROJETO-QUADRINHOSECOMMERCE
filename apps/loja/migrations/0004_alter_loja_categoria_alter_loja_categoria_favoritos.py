# Generated by Django 4.2.5 on 2023-10-10 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_loja_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='categoria',
            field=models.CharField(choices=[('DC', 'DC'), ('MARVEL', 'Marvel'), ('IMAGE COMICS', 'Image Comics'), ('CGC', 'CGC')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='loja',
            name='categoria_favoritos',
            field=models.CharField(choices=[('BATMAN', 'Batman'), ('SUPERMAN', 'Superman'), ('HOMEM ARANHA', 'Homem aranha'), ('VINGADORES', 'Vingadores'), ('LIGA DA JUSTIÇA', 'Liga da Justiça')], default=None, max_length=100),
        ),
    ]
