# Generated by Django 5.1.7 on 2025-03-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_configuracoes_veiculo', '0005_alter_configuracoesveiculo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracoesveiculo',
            name='top_cat',
            field=models.CharField(max_length=10, null=True, verbose_name='Top Cat da Configuração'),
        ),
    ]
