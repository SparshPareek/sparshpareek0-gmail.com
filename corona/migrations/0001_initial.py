# Generated by Django 3.0.4 on 2020-03-26 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='India',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cases', models.CharField(max_length=255)),
                ('active_cases', models.CharField(max_length=255)),
            ],
        ),
    ]
