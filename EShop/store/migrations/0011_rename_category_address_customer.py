# Generated by Django 3.2 on 2022-04-11 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_address_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='category',
            new_name='customer',
        ),
    ]
