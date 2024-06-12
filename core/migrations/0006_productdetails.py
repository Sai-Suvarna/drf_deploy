# Generated by Django 4.1.3 on 2024-06-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_image_word'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('item', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=20)),
                ('units', models.CharField(max_length=10)),
                ('thresholdValue', models.IntegerField()),
                ('image', models.JSONField()),
            ],
            options={
                'db_table': 'productDetails',
            },
        ),
    ]