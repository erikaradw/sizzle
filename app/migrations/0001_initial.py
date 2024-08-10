# Generated by Django 5.0.6 on 2024-05-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_artikel', models.IntegerField(unique=True)),
                ('judul_artikel', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kursus', models.IntegerField(unique=True)),
                ('nama_kursus', models.CharField(max_length=50, unique=True)),
                ('harga_kursus', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_resep', models.IntegerField(unique=True)),
                ('nama_resep', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
