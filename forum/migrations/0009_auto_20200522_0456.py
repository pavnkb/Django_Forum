# Generated by Django 3.0.5 on 2020-05-21 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20200522_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
