# Generated by Django 2.2.5 on 2019-09-18 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.CharField(max_length=200)),
                ('linha2', models.CharField(blank=True, max_length=200, null=True)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longetude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]