# Generated by Django 4.1.6 on 2023-02-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('numberOfAppearances', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
