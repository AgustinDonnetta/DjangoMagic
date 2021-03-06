# Generated by Django 3.1.1 on 2020-11-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('DNI', models.IntegerField()),
                ('born_date', models.DateField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
