# Generated by Django 2.1.3 on 2018-11-17 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20181112_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinglistindi',
            name='date_visit',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bookinglistorga',
            name='date_visit',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]