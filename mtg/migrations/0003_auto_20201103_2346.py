# Generated by Django 3.1.1 on 2020-11-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0002_auto_20201102_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='player',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
