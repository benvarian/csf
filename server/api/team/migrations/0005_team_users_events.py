# Generated by Django 4.2.3 on 2024-02-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_alter_team_total_mileage'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='users_events',
            field=models.TextField(default=''),
        ),
    ]
