# Generated by Django 3.1.2 on 2020-11-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misCar', '0003_carw_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('subtitulos', models.CharField(max_length=20)),
                ('titulo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]