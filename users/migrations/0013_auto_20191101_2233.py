# Generated by Django 2.2.1 on 2019-11-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191021_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cns',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, unique=True),
        ),
    ]
