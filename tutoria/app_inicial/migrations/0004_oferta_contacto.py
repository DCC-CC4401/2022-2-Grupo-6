# Generated by Django 3.2.12 on 2022-11-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inicial', '0003_auto_20221128_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='contacto',
            field=models.CharField(default=2234, max_length=255),
            preserve_default=False,
        ),
    ]
