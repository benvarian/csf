# Generated by Django 4.2.2 on 2023-07-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_reset_time_user_reset_token_alter_user_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='challenge_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]