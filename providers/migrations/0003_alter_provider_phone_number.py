# Generated by Django 3.2.5 on 2022-02-20 10:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20220220_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]