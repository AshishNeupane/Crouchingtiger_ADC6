# Generated by Django 3.0.1 on 2020-01-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Mobile', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
