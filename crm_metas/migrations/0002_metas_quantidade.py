# Generated by Django 5.1.7 on 2025-03-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_metas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metas',
            name='quantidade',
            field=models.IntegerField(choices=[(1, '01'), (2, '02'), (3, '03'), (4, '04'), (5, '05'), (6, '06'), (7, '07'), (8, '08'), (9, '09'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19')], null=True, verbose_name='Quantidade'),
        ),
    ]
