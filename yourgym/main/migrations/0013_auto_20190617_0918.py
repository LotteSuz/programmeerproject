# Generated by Django 2.2.1 on 2019-06-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
