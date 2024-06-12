# Generated by Django 4.2.13 on 2024-06-11 16:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Доступные символы @/./+/-/_', regex='^[\\w.@+-]+$')], verbose_name='Никнейм пользователя'),
        ),
    ]
