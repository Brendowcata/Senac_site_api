# Generated by Django 4.0.5 on 2022-07-09 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollmentmodel',
            name='title_enrollment',
        ),
    ]