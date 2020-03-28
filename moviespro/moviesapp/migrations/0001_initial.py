# Generated by Django 3.0 on 2020-03-28 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(unique=True)),
                ('movie_name', models.CharField(max_length=100)),
                ('timings', models.TimeField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]