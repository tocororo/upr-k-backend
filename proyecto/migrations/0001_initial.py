# Generated by Django 4.1.9 on 2023-12-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('lider_proyecto', models.CharField(max_length=250)),
                ('objetivos', models.CharField(max_length=250)),
                ('linea_de_investigacion', models.CharField(max_length=250)),
            ],
        ),
    ]
