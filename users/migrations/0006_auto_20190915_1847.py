# Generated by Django 2.2.1 on 2019-09-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
