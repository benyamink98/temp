# Generated by Django 2.2.6 on 2019-11-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20191123_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
