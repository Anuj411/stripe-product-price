# Generated by Django 4.2.16 on 2024-09-09 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organization_image_product_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='organization',
        ),
    ]
