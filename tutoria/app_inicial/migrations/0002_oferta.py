# Generated by Django 3.2.12 on 2022-11-28 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_inicial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nameTutor', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('materia', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('p_user', models.ForeignKey(db_column='p_user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pyme',
            },
        ),
    ]
