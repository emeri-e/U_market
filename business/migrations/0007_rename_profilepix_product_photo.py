# Generated by Django 4.0.8 on 2023-01-18 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_review_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ProfilePix',
            new_name='photo',
        ),
    ]