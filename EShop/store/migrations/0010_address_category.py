# Generated by Django 3.2 on 2022-04-11 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20220411_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]
