# Generated by Django 2.2.12 on 2022-08-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20220817_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestadorservico',
            name='data_de_entrada',
            field=models.DateTimeField(blank=True, max_length=10, null=True, verbose_name='Data de Entrada'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='data_de_entrada',
            field=models.DateTimeField(blank=True, max_length=10, null=True, verbose_name='Data de Entrada'),
        ),
    ]
