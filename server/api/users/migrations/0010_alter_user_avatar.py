# Generated by Django 4.2.3 on 2023-07-19 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(choices=[('avatar1.jpg', 'avatar 1'), ('avatar2.jpg', 'avatar 2'), ('avatar3.jpg', 'avatar 3'), ('avatar4.jpg', 'avatar 4'), ('avatar5.jpg', 'avatar 5'), ('avatar6.jpg', 'avatar 6')], default='avatar1.jpg', max_length=100),
        ),
    ]
