# Generated by Django 2.2.1 on 2019-06-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190611_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='available',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
