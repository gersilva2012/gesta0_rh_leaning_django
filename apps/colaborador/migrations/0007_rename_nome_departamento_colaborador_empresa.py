# Generated by Django 3.2.5 on 2021-08-11 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0006_auto_20210727_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colaborador',
            old_name='nome_departamento',
            new_name='empresa',
        ),
    ]