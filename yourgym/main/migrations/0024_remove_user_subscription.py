# Generated by Django 2.2.1 on 2019-06-23 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20190623_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subscription',
        ),
    ]
