# Generated by Django 5.0.4 on 2025-02-25 16:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uzum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzum',
            name='unique_id',
            field=models.CharField(blank=True, help_text='bu yerga hechnarsa kiritilmaydi', max_length=90, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='hato_boldi', message='bunda $ @ ^ kiritib bolmaydi ', regex='^(?=.*[A-Za-z])(?=.*\\d)(?=.*[@$!%*])[^?&^]{-}$')]),
        ),
    ]
