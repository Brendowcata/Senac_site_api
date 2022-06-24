# Generated by Django 4.0.5 on 2022-06-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_coursemodel_description_and_more'),
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universitymodel',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='courses', to='course.coursemodel'),
        ),
    ]
