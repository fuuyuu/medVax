# Generated by Django 2.2.1 on 2019-11-02 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20191101_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cns',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
