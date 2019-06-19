# Generated by Django 2.2.1 on 2019-06-16 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190614_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
            ],
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.DeleteModel(
            name='CartItems',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cartowner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='main.Cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='main.Stock'),
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='itemtype', through='main.CartItem', to='main.Stock'),
        ),
    ]