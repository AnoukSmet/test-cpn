# Generated by Django 3.1.4 on 2020-12-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20201215_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationlineitem',
            name='original_reservation',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='reservationlineitem',
            name='stripe_pid',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]