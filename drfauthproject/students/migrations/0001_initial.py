# Generated by Django 4.1.5 on 2023-01-05 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('stdNum', models.IntegerField(max_length=8, verbose_name='Student Number')),
                ('course', models.CharField(max_length=20, verbose_name='Course')),
            ],
        ),
    ]
