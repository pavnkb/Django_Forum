# Generated by Django 3.0.5 on 2020-05-20 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='content',
            new_name='desc',
        ),
    ]
