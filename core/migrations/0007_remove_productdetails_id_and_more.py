# Generated by Django 4.1.3 on 2024-06-04 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_productdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='productId',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
