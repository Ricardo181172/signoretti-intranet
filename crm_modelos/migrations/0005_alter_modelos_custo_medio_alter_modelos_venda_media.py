# Generated by Django 5.1.7 on 2025-03-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_modelos', '0004_remove_modelos_top_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelos',
            name='custo_medio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Custo Médio do Modelo'),
        ),
        migrations.AlterField(
            model_name='modelos',
            name='venda_media',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Venda Média do Modelo'),
        ),
    ]
