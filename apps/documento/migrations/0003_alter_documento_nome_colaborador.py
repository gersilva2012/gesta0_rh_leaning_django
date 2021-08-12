# Generated by Django 3.2.5 on 2021-08-12 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0012_auto_20210811_2250'),
        ('documento', '0002_rename_a_quem_pertence_documento_nome_colaborador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='nome_colaborador',
            field=models.ForeignKey(help_text='A quem pertence o arquivo', on_delete=django.db.models.deletion.PROTECT, to='colaborador.colaborador'),
        ),
    ]
