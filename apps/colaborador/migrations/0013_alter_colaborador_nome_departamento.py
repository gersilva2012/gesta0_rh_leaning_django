# Generated by Django 3.2.5 on 2021-08-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
        ('colaborador', '0012_auto_20210811_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='nome_departamento',
            field=models.ManyToManyField(help_text='Em qual setor', to='departamento.Departamento'),
        ),
    ]
