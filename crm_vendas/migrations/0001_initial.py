# Generated by Django 5.1.7 on 2025-03-29 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm_pedidos_venda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nf_venda', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_ultima_edicao', models.DateTimeField(auto_now=True, null=True)),
                ('pedido_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_pedidos_venda.pedidosvenda')),
            ],
            options={
                'db_table': 'crm_vendas',
                'ordering': ['pedido_venda'],
            },
        ),
    ]
