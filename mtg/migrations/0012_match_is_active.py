# Generated by Django 3.1.1 on 2020-11-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0011_auto_20201107_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]