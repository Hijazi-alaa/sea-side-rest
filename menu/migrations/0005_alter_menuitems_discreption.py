# Generated by Django 3.2 on 2022-04-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuitems_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='discreption',
            field=models.TextField(max_length=800),
        ),
    ]
