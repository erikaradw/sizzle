# Generated by Django 5.0.6 on 2024-05-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_delete_kategorikursus'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriKursus',
            fields=[
                ('id_kategori_kursus', models.AutoField(primary_key=True, serialize=False)),
                ('kategori_kursus', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
