# Generated by Django 5.1.5 on 2025-03-02 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uzum', '0002_uzum_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzum',
            name='tasnif',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
