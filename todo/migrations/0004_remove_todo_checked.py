# Generated by Django 3.1.3 on 2020-11-30 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201129_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='checked',
        ),
    ]
