# Generated by Django 4.0.8 on 2023-01-16 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='id',
            new_name='Puuid',
        ),
    ]
