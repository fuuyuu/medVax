# Generated by Django 2.2.1 on 2019-09-15 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_profile_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cpf',
            field=models.CharField(default='17332096030', max_length=14),
            preserve_default=False,
        ),
    ]
