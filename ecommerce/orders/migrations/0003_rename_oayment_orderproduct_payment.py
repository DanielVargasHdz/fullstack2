# Generated by Django 5.0.6 on 2024-06-11 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderproduct_color_remove_orderproduct_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderproduct',
            old_name='oayment',
            new_name='payment',
        ),
    ]
