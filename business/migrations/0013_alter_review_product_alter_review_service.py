# Generated by Django 4.0.8 on 2023-01-24 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0012_product_average_rating_product_views_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='business.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='service',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='business.service'),
        ),
    ]
