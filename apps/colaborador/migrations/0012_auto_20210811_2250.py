# Generated by Django 3.2.5 on 2021-08-12 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
        ('colaborador', '0011_auto_20210811_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colaborador',
            name='nome_departamento',
        ),
        migrations.AddField(
            model_name='colaborador',
            name='nome_departamento',
            field=models.ManyToManyField(help_text='Em qual setor', null=True, to='departamento.Departamento'),
        ),
    ]