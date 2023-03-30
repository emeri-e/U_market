# Generated by Django 4.0.8 on 2023-01-20 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0010_remove_business_category_alter_business_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL),
        ),
    ]
