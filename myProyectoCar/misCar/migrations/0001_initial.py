# Generated by Django 2.2.16 on 2020-10-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insumoss',
            fields=[
                ('nombre', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('contraseña1', models.CharField(max_length=40)),
                ('contraseña2', models.CharField(max_length=40)),
            ],
        ),
    ]