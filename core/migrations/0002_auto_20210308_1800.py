# Generated by Django 3.1.7 on 2021-03-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracoes',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]
