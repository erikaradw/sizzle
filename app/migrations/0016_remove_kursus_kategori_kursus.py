# Generated by Django 5.0.6 on 2024-05-28 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_kategorikursus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kursus',
            name='kategori_kursus',
        ),
    ]
