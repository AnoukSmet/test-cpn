# Generated by Django 3.1.4 on 2020-12-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='main_image',
            field=models.BooleanField(default=False),
        ),
    ]
