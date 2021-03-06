# Generated by Django 3.1.1 on 2020-11-08 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtg', '0012_match_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn_number', models.IntegerField()),
                ('play_land', models.BooleanField(default=False)),
                ('play_creatures', models.CharField(max_length=15)),
                ('play_another_thing', models.CharField(blank=True, max_length=20)),
                ('attack', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('player_1_life', models.IntegerField()),
                ('player_2_life', models.IntegerField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Match', to='mtg.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Player', to='mtg.player')),
            ],
        ),
    ]
