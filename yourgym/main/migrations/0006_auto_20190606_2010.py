# Generated by Django 2.2.1 on 2019-06-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190606_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='document',
            field=models.FileField(default=None, upload_to='documents/'),
        ),
    ]