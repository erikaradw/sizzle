# Generated by Django 5.0.6 on 2024-05-28 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_kategorikursus_kursus_kategori_kursus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kursus',
            name='kategori_kursus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='kursuss', to='app.kategoriresep'),
        ),
    ]
