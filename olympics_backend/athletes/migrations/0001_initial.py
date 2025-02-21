# Generated by Django 5.0.7 on 2024-08-01 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ultitable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=255)),
                ('conference', models.CharField(max_length=255)),
                ('division', models.CharField(max_length=10)),
                ('ncaa_sport', models.CharField(max_length=255)),
                ('olympic_sport', models.CharField(max_length=255)),
                ('country_team', models.CharField(max_length=100)),
                ('olympic_role', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ultitable',
            },
        ),
    ]
