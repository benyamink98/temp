# Generated by Django 2.2.6 on 2019-11-27 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_productfilter_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfilter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
