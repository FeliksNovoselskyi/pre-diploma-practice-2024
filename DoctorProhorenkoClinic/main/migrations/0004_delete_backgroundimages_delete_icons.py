# Generated by Django 4.2.7 on 2024-06-19 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_backgroundimages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BackgroundImages',
        ),
        migrations.DeleteModel(
            name='Icons',
        ),
    ]
