# Generated by Django 4.1.13 on 2023-11-14 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('cargo', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('imagen', models.CharField(max_length=250)),
            ],
        ),
    ]