# Generated by Django 4.1.6 on 2023-02-09 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_stone_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weilder',
            name='is_hero',
            field=models.BooleanField(choices=[('Yes', True), ('No', False)]),
        ),
    ]
