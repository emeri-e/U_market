# Generated by Django 4.0.8 on 2023-01-18 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_cart_user_alter_product_profilepix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='count',
            new_name='product_count',
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='business.product')),
            ],
        ),
    ]
