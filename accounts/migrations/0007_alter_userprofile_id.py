# Generated by Django 4.0.8 on 2023-01-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
