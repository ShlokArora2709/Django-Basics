# Generated by Django 5.0.4 on 2024-04-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelloWorld', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(default='2022-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
