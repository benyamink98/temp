# Generated by Django 2.2.6 on 2019-11-23 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20191123_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='successfulpayment',
            name='order',
        ),
        migrations.AddField(
            model_name='successfulpayment',
            name='orderitems',
            field=models.ManyToManyField(to='shop.Cart'),
        ),
    ]