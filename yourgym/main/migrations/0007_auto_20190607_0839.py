# Generated by Django 2.2.1 on 2019-06-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190606_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='document',
            field=models.FileField(default=None, upload_to='main/documents/'),
        ),
    ]
