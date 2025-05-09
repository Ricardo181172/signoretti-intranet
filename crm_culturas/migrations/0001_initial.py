# Generated by Django 5.1.7 on 2025-03-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_ultima_edicao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'crm_culturas',
                'ordering': ['descricao'],
            },
        ),
    ]
