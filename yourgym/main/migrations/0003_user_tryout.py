# Generated by Django 2.2.1 on 2019-06-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190612_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tryout',
            field=models.CharField(max_length=200, null=True),
        ),
    ]