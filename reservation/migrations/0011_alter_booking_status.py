# Generated by Django 3.2 on 2022-04-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_auto_20220407_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.BooleanField(default=0, verbose_name='Approved'),
        ),
    ]