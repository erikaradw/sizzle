# Generated by Django 5.0.6 on 2024-05-28 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_kategorikursus'),
    ]

    operations = [
        migrations.AddField(
            model_name='kursus',
            name='kategori_kursus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.kategorikursus'),
        ),
    ]
