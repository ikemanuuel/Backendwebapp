# Generated by Django 4.2.6 on 2023-12-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_alter_item_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]