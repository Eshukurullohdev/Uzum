# Generated by Django 5.0.4 on 2025-02-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uzum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=100)),
                ('sharh', models.CharField(max_length=100)),
                ('bolib_tolash', models.IntegerField(default=0)),
                ('skidka', models.IntegerField(default=0)),
                ('narx', models.IntegerField(default=0)),
            ],
        ),
    ]
