# Generated by Django 3.1.4 on 2020-12-31 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20201211_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
