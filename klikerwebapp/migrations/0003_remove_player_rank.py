# Generated by Django 3.0.1 on 2019-12-22 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klikerwebapp', '0002_player_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='rank',
        ),
    ]
