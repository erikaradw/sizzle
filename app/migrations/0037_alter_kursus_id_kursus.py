# Generated by Django 5.0.6 on 2024-05-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_remove_kursus_kategori_kursus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kursus',
            name='id_kursus',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
